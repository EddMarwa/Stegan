import tkinter as tk
from tkinter import filedialog, messagebox
from encoding import encode_message
from decoding import decode_message

# Function to handle the encoding process
def encode():
    image_path = filedialog.askopenfilename(title="Select Image for Encoding")
    if not image_path:
        return

    message = message_entry.get()
    if not message:
        messagebox.showerror("Error", "Please enter a message to encode.")
        return

    output_path = filedialog.asksaveasfilename(defaultextension=".png", title="Save Encoded Image As")
    if not output_path:
        return

    password = password_entry.get()
    if not password:
        messagebox.showerror("Error", "Please enter a password.")
        return

    try:
        encode_message(image_path, message, output_path, password)
        messagebox.showinfo("Success", f"Message encoded and saved to {output_path}")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to encode message: {e}")

# Function to handle the decoding process
def decode():
    image_path = filedialog.askopenfilename(title="Select Image for Decoding")
    if not image_path:
        return

    password = password_entry.get()
    if not password:
        messagebox.showerror("Error", "Please enter a password.")
        return

    try:
        decoded_message = decode_message(image_path, password)
        messagebox.showinfo("Decoded Message", f"Decoded message: {decoded_message}")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to decode message: {e}")

# Set up the GUI window
root = tk.Tk()
root.title("Steganography Tool")
root.geometry("400x250")

# Label and Entry for the message to be encoded
message_label = tk.Label(root, text="Message to Encode:")
message_label.pack(pady=10)

message_entry = tk.Entry(root, width=50)
message_entry.pack(pady=5)

# Label and Entry for the password
password_label = tk.Label(root, text="Password:")
password_label.pack(pady=10)

password_entry = tk.Entry(root, show="*", width=50)
password_entry.pack(pady=5)

# Encode Button
encode_button = tk.Button(root, text="Encode Message", command=encode)
encode_button.pack(pady=10)

# Decode Button
decode_button = tk.Button(root, text="Decode Message", command=decode)
decode_button.pack(pady=10)

# Start the GUI loop
root.mainloop()
