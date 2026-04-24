from detector.lsb_detector import analyze_lsb
from detector.histogram_detector import analyze_histogram
from flask import Flask, render_template, request, send_file
import os
from encode import encode_message
from decode import decode_message

app = Flask(__name__)

UPLOAD_FOLDER: str = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

#Home page
@app.route('/')
def home():
    return render_template('index.html')

#Encode route
@app.route('/encode', methods=['POST'])
def encode():
    if 'image' not in request.files:
        return "No file uploaded"
    
    file = request.files['image']
    message = request.form.get('message', '')
    
    if file.filename == '':
        return "No selected file"
    
    filename = file.filename or "temp.png"
    filepath = os.path.join(UPLOAD_FOLDER, filename)
    file.save(filepath)
    
    output_path = os.path.join(UPLOAD_FOLDER, "encoded.png")
    result = encode_message(filepath, message, output_path)
    
    if "successfully" in result:
        return send_file(output_path, as_attachment=True)
    else:
        return result

#Decode route
@app.route('/decode', methods=['POST'])
def decode():
    if 'image' not in request.files:
        return "No file uploaded"
    
    file = request.files['image']
    
    if file.filename == '':
        return "No selected file"
    
    filename = file.filename or "temp.png"
    filepath = os.path.join(UPLOAD_FOLDER, filename)
    file.save(filepath)
    
    message = decode_message(filepath)
    
    return render_template('index.html', decoded_message=message)

#Detect route
@app.route('/detect', methods=['POST'])
def detect():
    if 'image' not in request.files:
        return "No file uploaded"
    
    file = request.files['image']
    
    if file.filename == '':
        return "No selected file"
    
    filename = file.filename or "temp.png"
    filepath = os.path.join(UPLOAD_FOLDER, filename)
    file.save(filepath)
    
    #Run detection
    lsb_text, lsb_score = analyze_lsb(filepath)
    hist_text, hist_score = analyze_histogram(filepath)
    
    message = decode_message(filepath)
    
    #Final decision 
    if message and message != "No hidden message found":
        final_result = "Hidden Data Confirmed"
        final_score = 95
        
    #weighted scoring
    else:
        final_score = int((lsb_score * 0.7) + hist_score * 0.3)
    
        if lsb_score <30 and hist_score < 50:
            final_result = "Clean Image"
            final_score = 10
        elif final_score > 80:
            final_result = "Suspicious (But not confirmed)"
        elif final_score > 60:
            final_result = "Possible Hidden Data"
        elif final_score > 40:
            final_result = "Low Probability of Hidden Data (Check Recommended)"
        else:
            final_result = "Likely Clean Image"
    
    return render_template('index.html', lsb_result=lsb_text, hist_result=hist_text, final_result=final_result,confidence=final_score)

if __name__ == '__main__':
    app.run(debug=True)