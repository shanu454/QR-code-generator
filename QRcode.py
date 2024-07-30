import tkinter as tk
from tkinter import messagebox
import qrcode
from PIL import Image, ImageTk

def generate_qr():
    data = entry.get()
    if data.strip() == "":
        messagebox.showerror("Error", "Please enter some data to generate a QR code.")
        return
    
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    
    qr.add_data(data)
    qr.make(fit=True)
    
    img = qr.make_image(fill='black', back_color='white')
    
    filename = "qrcode.png"
    img.save(filename)
    
    img = Image.open(filename)
    img = ImageTk.PhotoImage(img)
    
    qr_label.config(image=img)
    qr_label.image = img
    messagebox.showinfo("Success", f"QR code generated and saved as {filename}")

app = tk.Tk()
app.title("QR Code Generator")

frame = tk.Frame(app)
frame.pack(padx=10, pady=10)

label = tk.Label(frame, text="Enter data to encode:")
label.grid(row=0, column=0, pady=5)

entry = tk.Entry(frame, width=40)
entry.grid(row=1, column=0, pady=5)

button = tk.Button(frame, text="Generate QR Code", command=generate_qr)
button.grid(row=2, column=0, pady=5)

qr_label = tk.Label(frame)
qr_label.grid(row=3, column=0, pady=5)

app.mainloop()