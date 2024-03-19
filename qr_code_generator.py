import qrcode
import tkinter as tk
from tkinter import messagebox
from PIL import ImageTk, Image
from io import BytesIO

def generate_qr():
    data = qr_data.get()
    if data:
        qr_data_list = [d.strip() for d in data.split(',')]  # Split data by comma and remove leading/trailing whitespace
        for index, qr_data_item in enumerate(qr_data_list):
            qr = qrcode.QRCode(
                version=1,
                error_correction=qrcode.constants.ERROR_CORRECT_L,
                box_size=10,
                border=4,
            )
            qr.add_data(qr_data_item)
            qr.make(fit=True)
            img = qr.make_image(fill_color="black", back_color="white")

            # Display QR code within the application
            qr_image = ImageTk.PhotoImage(img)
            qr_images.append((qr_image, qr_data_item))
            qr_label = tk.Label(root, image=qr_image)
            qr_label.grid(row=index + 4, column=0, padx=10, pady=10, sticky="w")
            qr_label.bind("<Button-1>", lambda event, index=index: copy_text(qr_images[index][1]))

    else:
        messagebox.showerror("Error", "Please enter some data for the QR code")

def copy_text(text):
    root.clipboard_clear()
    root.clipboard_append(text)
    messagebox.showinfo("Copied", "Text copied to clipboard!")

# Create main window
root = tk.Tk()
root.title("QR Code Generator")

# Create input label and entry
label = tk.Label(root, text="Enter data for QR Code (separate with commas):")
label.grid(row=0, column=0, padx=10, pady=10, sticky="w")
qr_data = tk.Entry(root)
qr_data.grid(row=1, column=0, padx=10, pady=5, sticky="ew")

# Create generate button
generate_button = tk.Button(root, text="Generate QR Codes", command=generate_qr)
generate_button.grid(row=2, column=0, padx=10, pady=5, sticky="ew")

# Create label to display generated QR codes
qr_images = []

# Run the application
root.mainloop()
