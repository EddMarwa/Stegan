from PIL import Image
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes
from cryptography.fernet import Fernet
import base64
import os

# Function to generate a key based on a password and salt
def generate_key_from_password(password: str, salt: bytes):
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=100000
    )
    key = base64.urlsafe_b64encode(kdf.derive(password.encode()))
    return key

# Function to decrypt a message using a password
def decrypt_message_with_password(encrypted_message: bytes, password: str, salt: bytes):
    key = generate_key_from_password(password, salt)
    cipher = Fernet(key)
    return cipher.decrypt(encrypted_message).decode()

def decode_message(image_path, password):
    img = Image.open(image_path)
    img_data = img.getdata()

    binary_message = ""
    for pixel in img_data:
        binary_message += str(pixel[0] & 1)

    # Convert binary string back to bytes
    byte_array = bytearray()
    for i in range(0, len(binary_message), 8):
        byte_array.append(int(binary_message[i:i+8], 2))

    # Extract salt from the beginning of the message (assuming it's 16 bytes)
    salt = byte_array[:16]
    encrypted_message = bytes(byte_array[16:])

    # Decrypt and decode the message
    decrypted_message = decrypt_message_with_password(encrypted_message, password, salt)
    return decrypted_message
