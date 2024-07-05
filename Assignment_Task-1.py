import tkinter as tk
from tkinter import filedialog, messagebox, simpledialog
from PIL import Image, ImageTk
import os

def open_image():
    folder_path = filedialog.askdirectory(title="Select Folder")
    if not folder_path:
        return

    image_name = simpledialog.askstring("Input", "Enter the name of the image (with extension):")
    if not image_name:
        return

    image_path = os.path.join(folder_path, image_name)
    if not os.path.exists(image_path):
        messagebox.showerror("Error", f"The file {image_name} does not exist in the selected folder.")
        return

    img = Image.open(image_path)
    img = img.resize((400, 400), Image.LANCZOS)
    img_tk = ImageTk.PhotoImage(img)

    panel.config(image=img_tk)
    panel.image = img_tk

root = tk.Tk()
root.title("Image Viewer")
root.geometry("600x400")

panel = tk.Label(root)
panel.pack(pady=20)

open_button = tk.Button(root, text="Open Image", command=open_image)
open_button.pack()

root.mainloop()
