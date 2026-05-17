# 🕵️‍♂️ Steganography Studio (Web App)

**🚀 Live Demo:** [https://stegano-studio-d3f7.onrender.com/](https://stegano-studio-d3f7.onrender.com/)

A modern, interactive, and beautiful web-based steganography tool that allows users to securely hide, extract, and detect secret messages inside images.

## 📖 About the Project
Steganography is the practice of concealing information within another medium (like an image) so that the presence of the message is hidden from plain sight. This project provides a sleek, user-friendly interface powered by a robust Python backend to:
- **Encode** a secret message inside an image.
- **Decode** and extract hidden messages.
- **Detect** steganography using advanced statistical analysis (LSB and Histogram detection).

This tool uses the **Least Significant Bit (LSB)** technique to embed data directly into pixel values, ensuring no noticeable visual changes to the human eye.

## ✨ Features
- **Hide & Extract**: Easily upload images to encode secret text or decode existing hidden messages.
- **Steganography Detection**: Analyzes images to detect tampering using LSB patterns and Histogram variations, providing a confidence score.
- **Stunning UI/UX**: Features a fully responsive, modern glassmorphism design with fluid animations and a sleek dark mode.
- **Fast Processing**: Python-powered backend ensures quick image processing and data extraction.
- **Download Ready**: Instantly download your encoded images for secure sharing.

## 🛠️ Tech Stack
- **Frontend**: HTML5, CSS3 (Glassmorphism), Vanilla JavaScript.
- **Backend**: Python, Flask.
- **Image Processing/Analysis**: NumPy, Pillow.

## ⚙️ How It Works
1. **Encoding**: The user uploads an image and enters a secret message. The message is converted into binary, and the data is hidden inside the least significant bits of the image pixels.
2. **Decoding**: The application reads the pixel data of an encoded image, extracts the hidden binary data, and converts it back into readable text.
3. **Detection**: The system runs mathematical models against the image's color histogram and bit planes to identify anomalies commonly left behind by steganography.

## 🚀 Getting Started

### Prerequisites
Make sure you have [Python 3.x](https://www.python.org/downloads/) installed on your machine.

### Installation
1. **Clone the Repository**
   ```bash
   git clone https://github.com/PrabhSaran-07/stegano-web-app.git
   cd stegano-web-app/Backend
   ```

2. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the Application**
   ```bash
   python app.py
   ```

4. **Open in Browser**
   Navigate to `http://127.0.0.1:5000` in your web browser.

## 📂 Project Structure
```text
stegano-web-app/
├── Backend/
│   ├── app.py                 # Main Flask server entry point
│   ├── encode.py              # Steganography encoding logic
│   ├── decode.py              # Steganography decoding logic
│   ├── detector/              # LSB & Histogram detection algorithms
│   ├── static/                # CSS styles and JavaScript logic
│   ├── templates/             # HTML templates (index.html)
│   ├── uploads/               # Temporary storage for processing
│   └── requirements.txt       # Python dependencies
└── README.md
```

## 🎮 Usage
- **Encode Message**: Upload an image, enter your secret message, and click "Encode & Download".
- **Decode Message**: Upload a previously encoded image and click "Decode Message" to reveal the secret text.
- **Detect Hidden Data**: Upload a suspicious image and click "Detect Steganography" to analyze it for hidden data signatures.

## ⚠️ Limitations
- **Format**: Works best with **PNG** images as they use lossless compression. (JPG compression will destroy the hidden LSB data).
- **Security**: The data is hidden but not encrypted. For extreme security, encrypt your text *before* encoding it into the image.
- **Capacity**: Extremely large messages in small images may begin to degrade visual quality.
