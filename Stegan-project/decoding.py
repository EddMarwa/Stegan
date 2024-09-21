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

def decrypt_message(encrypted_message):
    return cipher.decrypt(encrypted_message).decode()

def decode_message(image_path):
    img = Image.open(image_path)
    img_data = img.getdata()
    
    binary_message = ""
    for pixel in img_data:
        binary_message += str(pixel[0] & 1)

    # Convert binary string back to bytes
    byte_array = bytearray()
    for i in range(0, len(binary_message), 8):
        byte_array.append(int(binary_message[i:i+8], 2))
    
    # Decrypt and decode the message
    decrypted_message = decrypt_message(byte_array)
    return decrypted_message
