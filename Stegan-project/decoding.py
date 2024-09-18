from PIL import Image

def decode_message(image_path):
    img = Image.open(image_path)
    img_data = img.getdata()
    
    binary_message = ""
    for pixel in img_data:
        binary_message += str(pixel[0] & 1)
    
    chars = [binary_message[i:i+8] for i in range(0, len(binary_message), 8)]
    decoded_message = ''.join([chr(int(char, 2)) for char in chars if int(char, 2) != 0])
    
    return decoded_message
