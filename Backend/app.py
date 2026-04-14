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

if __name__ == '__main__':
    app.run(debug=True)