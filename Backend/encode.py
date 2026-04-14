from PIL import Image
from typing import Union

def encode_message(image_path: str, message: str, output_path: str) -> str:
    img = Image.open(image_path)
    encoded = img.copy()
    width, height = img.size
    
    message += "###" #delimiter to mark the end of the message
    data_index = 0
    binary_message = ''.join(format(ord(i), '08b') for i in message) #converts message into binary form
    
    for y in range(height):  #loop through pixels
        for x in range(width):
            pixel_data: Union[int, float, tuple, None] = img.getpixel((x, y))
            if pixel_data is None:
                continue
            
            # Convert pixel to list for manipulation
            if isinstance(pixel_data, (tuple, list)):
                pixel = [int(p) for p in pixel_data]
            else:
                pixel = [int(pixel_data)]
            
            for n in range(min(3, len(pixel))): #RGB channels
                if data_index < len(binary_message):
                    pixel[n] = pixel[n] & ~1 | int(binary_message[data_index])
                    data_index += 1
                    
            encoded.putpixel((x, y), tuple(pixel) if len(pixel) > 1 else pixel[0])
            
            if data_index >= len(binary_message):
                encoded.save(output_path)
                return "Message encoded successfully!"
            
    return "Message too long to encode in this image"