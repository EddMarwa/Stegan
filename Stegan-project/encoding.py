from PIL import Image

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

