Stegano Web App
A simple and interactive web-based steganography tool that allows users to hide and extract secret messages inside images.

About the Project
Steganography is the technique of hiding information inside another medium (like images) so that the presence of the message is not obvious.
This project provides an easy-to-use web interface where users can:
Encode (hide) a secret message inside an image
Decode (extract) a hidden message from an image
Most web-based steganography tools use techniques like LSB (Least Significant Bit) manipulation to embed data into pixel values without noticeable visual changes .

 Features
 Upload images and hide secret messages
 Extract hidden messages from encoded images
 Simple and user-friendly interface
 Fast processing in the browser
 Download encoded images
 
 Tech Stack
HTML
CSS
JavaScript 
Python

How It Works
Encoding Process
User uploads an image
Enters a secret message
The message is converted into binary
Data is hidden inside image pixels (LSB method)
Decoding Process
User uploads encoded image
App reads pixel data
Extracts hidden binary data
Converts it back into readable text

Getting Started
1. Clone the Repository
git clone https://github.com/PrabhSaran-07/stegano-web-app.git
2. Open the Project
Navigate to the project folder
Open index.html in your browser or run using python app.py and open the project using localhost

Project Structure
stegano-web-app/
|──Backend
  │── index.html
  │── style.css
  │── script.js / tools.js
  │── encode.js
  │── decode.js
  │── uploads/

Usage
Encode Message
Upload an image
Enter your secret message
Click Encode
Download the new image
Decode Message
Upload encoded image
Click Decode
View hidden message

Limitations
Works best with PNG images (lossless format)
Not highly secure (no encryption applied)
Large messages may affect image quality
