from PIL import Image
from PIL import Image
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes
from cryptography.fernet import Fernet
import base64
import os

# Function to generate a key based on a password
def generate_key_from_password(password: str, salt: bytes):
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=100000
    )
    key = base64.urlsafe_b64encode(kdf.derive(password.encode()))
    return key

# Function to encrypt a message using a password
def encrypt_message_with_password(message: str, password: str):
    salt = os.urandom(16)  # Generate a random salt
    key = generate_key_from_password(password, salt)
    cipher = Fernet(key)
    encrypted_message = cipher.encrypt(message.encode())
    return encrypted_message, salt  # Return encrypted message and salt

def encode_message(image_path, message, output_path, password):
    encrypted_message, salt = encrypt_message_with_password(message, password)
    binary_message = ''.join([format(byte, '08b') for byte in encrypted_message])  # Convert message to binary

    img = Image.open(image_path)
    img_data = img.getdata()

    new_data = []
    msg_index = 0
    for pixel in img_data:
        if msg_index < len(binary_message):
            new_pixel = list(pixel)
            new_pixel[0] = (pixel[0] & ~1) | int(binary_message[msg_index])
            new_data.append(tuple(new_pixel))
            msg_index += 1
        else:
            new_data.append(pixel)
    
    img.putdata(new_data)
    img.save(output_path)
    print(f"Message encoded and saved to {output_path}")


def encode_message(image_path, message, output_path):
    img = Image.open(image_path)
    binary_message = ''.join([format(ord(char), '08b') for char in message])
    img_data = img.getdata()
    
    new_data = []
    msg_index = 0
    for pixel in img_data:
        if msg_index < len(binary_message):
            new_pixel = list(pixel)
            new_pixel[0] = (pixel[0] & ~1) | int(binary_message[msg_index])
            new_data.append(tuple(new_pixel))
            msg_index += 1
        else:
            new_data.append(pixel)
    
    img.putdata(new_data)
    img.save(output_path)
    print(f"Message encoded and saved to {output_path}")

def encode_message(image_path, message, output_path):
    img = Image.open(image_path)
    capacity = image_capacity(image_path)

    if len(message) * 8 > capacity:
        raise ValueError("Message is too large to hide in this image.")

    binary_message = ''.join([format(ord(char), '08b') for char in message])
    img_data = img.getdata()

    new_data = []
    msg_index = 0
    for pixel in img_data:
        if msg_index < len(binary_message):
            new_pixel = list(pixel)
            new_pixel[0] = (pixel[0] & ~1) | int(binary_message[msg_index])
            new_data.append(tuple(new_pixel))
            msg_index += 1
        else:
            new_data.append(pixel)

    img.putdata(new_data)
    img.save(output_path)
    print(f"Message encoded and saved to {output_path}")

def image_capacity(image_path):
    img = Image.open(image_path)
    width, height = img.size
    return width * height * 3 // 8  

from PIL import Image
from cryptography.fernet import Fernet

# Encryption key (you can save this securely in a file or environment variable)
key = Fernet.generate_key()
cipher = Fernet(key)

def encrypt_message(message):
    return cipher.encrypt(message.encode())

def encode_message(image_path, message, output_path):
    encrypted_message = encrypt_message(message)
    binary_message = ''.join([format(byte, '08b') for byte in encrypted_message])

    img = Image.open(image_path)
    img_data = img.getdata()
    
    new_data = []
    msg_index = 0
    for pixel in img_data:
        if msg_index < len(binary_message):
            new_pixel = list(pixel)
            new_pixel[0] = (pixel[0] & ~1) | int(binary_message[msg_index])
            new_data.append(tuple(new_pixel))
            msg_index += 1
        else:
            new_data.append(pixel)
    
    img.putdata(new_data)
    img.save(output_path)
    print(f"Message encoded and saved to {output_path}")
