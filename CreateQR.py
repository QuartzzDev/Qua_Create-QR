######################### 
#       QuartzzDev      #
#########################

import cv2
import qrcode
import tkinter as tk
from tkinter import simpledialog, messagebox

def create_qr_code(data):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    return img

def show_qr_code(data):
    img = create_qr_code(data)
    img.show()

def edit_qr_code(data):
    root = tk.Tk()
    root.title("QR Code Editor")

    def add_text():
        additional_text = additional_text_entry.get()
        current_content = content_entry.get()
        new_content = f"{current_content}\n{additional_text}"       #<-- New QR Text here
        content_entry.delete(0, tk.END)
        content_entry.insert(0, new_content)

    def save_changes():
        title = title_entry.get()
        content = content_entry.get()
        edited_data = f"{title} {content}"
        show_qr_code(edited_data)
        root.destroy()

    title_label = tk.Label(root, text="Title:")
    title_label.pack()

    title_entry = tk.Entry(root)
    title_entry.pack()

    content_label = tk.Label(root, text="Content:")
    content_label.pack()

    content_entry = tk.Entry(root)
    content_entry.pack()

    additional_text_label = tk.Label(root, text="Additional Text:")
    additional_text_label.pack()

    additional_text_entry = tk.Entry(root)
    additional_text_entry.pack()

    add_text_button = tk.Button(root, text="Add Text", command=add_text)
    add_text_button.pack()

    save_button = tk.Button(root, text="Save Changes", command=save_changes)
    save_button.pack()

    root.mainloop()

def main():
    user_choice = simpledialog.askstring("Input", "Enter QR Code Data:")
    
    if user_choice:
        qr_code_data = user_choice

        # Check if user wants to edit QR code
        edit_choice = messagebox.askyesno("Edit QR Code", "Do you want to edit the QR code?")
        
        if edit_choice:
            edit_qr_code(qr_code_data)
        else:
            show_qr_code(qr_code_data)

if __name__ == "__main__":
    main()
