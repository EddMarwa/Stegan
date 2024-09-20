from encoding import encode_message
from decoding import decode_message


def main():
    choice = input("Enter 'e' to encode or 'd' to decode: ")
    if choice == 'e':
        image_path = input("Enter the image path (e.g., images/test_image.png): ")
        message = input("Enter the message to hide: ")
        output_path = input("Enter the output image path (e.g., images/output_image.png): ")
        encode_message(image_path, message, output_path)
    elif choice == 'd':
        image_path = input("Enter the image path to decode (e.g., images/output_image.png): ")
        decoded_message = decode_message(image_path)
        print(f"Decoded message: {decoded_message}")
    else:
        print("Invalid choice. Please enter 'e' to encode or 'd' to decode.")

if __name__ == "__main__":
    main()

# Error handling