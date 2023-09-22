from tkinter import Tk, Button, Label, filedialog
from PIL import Image
import os

# Conversion function
def convert_to_webp(input_folder, output_folder):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    input_files = os.listdir(input_folder)

    for filename in input_files:
        if filename.lower().endswith((".jpg", ".jpeg", ".png")):
            input_path = os.path.join(input_folder, filename)
            output_path = os.path.join(output_folder, os.path.splitext(filename)[0] + ".webp")

            # Convert and compress JPG, JPEG or PNG to WebP
            img = Image.open(input_path)
            img.save(output_path, "webp", quality=80)  # You can adjust the quality according to your desire

    print("Dönüştürme işlemi tamamlandı.")

# File selection function    
def select_folders():
    input_folder = filedialog.askdirectory(title="Giriş Klasörünü Seçin")
    output_folder = filedialog.askdirectory(title="Çıkış Klasörünü Seçin")

    if input_folder and output_folder:
        convert_to_webp(input_folder, output_folder)

# Create the Tkinter window
root = Tk()
root.title("WebP Dönüştürücü")

# Add labels and buttons
label = Label(root, text="Lütfen giriş ve çıkış klasörlerini seçin.")
label.pack(pady=10)

select_button = Button(root, text="Klasörleri Seç", command=select_folders)
select_button.pack()

root.mainloop()
