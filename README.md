# Stegan
Sample skeleton 
# 1
Steganography Project Skeleton
This project implements basic steganography techniques for securely embedding and extracting messages within digital images. The program will support encoding and decoding functionalities, allowing users to hide sensitive information within the least significant bits (LSBs) of image pixels. The initial setup includes the following modules:

1. **Image Processing:** Loading, manipulating, and saving images.
2. **Encoding:** Embedding a secret message into an image.
3. **Decoding:** Extracting the hidden message from the image.
4. **User Interface:** Command-line interface for user interaction.

The project will use the Python Imaging Library (PIL) for image processing and ensure the hidden message remains invisible to the human eye.


# 2
To begin, we will start by setting up the basic structure of the project. <br>
This includes creating a main script to handle the user inputs and coordinate the encoding and decoding processes. We'll also define functions for reading and writing images using the PIL library, ensuring that the images are processed in a way that allows us to manipulate the pixel data.<br> 
The encoding function will take a message and embed it into the image's pixels, while the decoding function will retrieve the hidden message. Each step will be modularized to maintain clarity and ease of maintenance.


