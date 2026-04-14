from PIL import Image
from typing import Union

def decode_message(image_path: str) -> str:
    img = Image.open(image_path)
    width, height = img.size
    
    binary_data = ""
    decoded_message = ""
    
    for y in range(height):
        for x in range(width):
            pixel: Union[int, float, tuple, None] = img.getpixel((x, y))
            if pixel is None:
                continue
            
            # Handle both RGB tuples and grayscale values
            if isinstance(pixel, (tuple, list)):
                for n in range(min(3, len(pixel))): #RGB channels
                    binary_data += str(int(pixel[n]) & 1)
            else:
                # Grayscale image
                binary_data += str(int(pixel) & 1)
                
    # Split binary into chunks of 8 bits
    all_bytes = [binary_data[i:i+8] for i in range(0, len(binary_data), 8)] 
    
    for byte in all_bytes:
        decoded_message += chr(int(byte, 2))
        if decoded_message.endswith("###"):
            return decoded_message[:-3]
        
    return "No hidden message found"