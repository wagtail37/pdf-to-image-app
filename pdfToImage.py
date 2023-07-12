import os
import tkinter as tk
from tkinter import filedialog
from pdf2image import convert_from_path

# popplerのパス
poppler_path = r"C:\Users\wagta\Documents\その他\pdf-to-image-app\poppler\Library\bin"

# 変換した画像を保存するリスト
images = []

def convert_pdf_to_images():
    global images
    # ユーザーがPDFファイルを選択できるダイアログを表示
    file_path = filedialog.askopenfilename()

    # 選択されたPDFを画像に変換
    images = convert_from_path(file_path, poppler_path=poppler_path)

def download_images():
    global images
    # ユーザーがディレクトリを選択できるダイアログを表示
    dir_path = filedialog.askdirectory()

    # 選択したディレクトリに画像を保存
    for i, image in enumerate(images):
        image.save(os.path.join(dir_path, 'img' + str(i) + '.jpg'), 'JPEG')

# Tkinterのウィンドウを作成
root = tk.Tk()
root.title("PDF to Image Converter")

# 変換ボタンを作成
convert_button = tk.Button(root, text="Convert PDF to Images", command=convert_pdf_to_images)
convert_button.pack()

# ダウンロードボタンを作成
download_button = tk.Button(root, text="Download Images", command=download_images)
download_button.pack()

# Tkinterのイベントループを開始
root.mainloop()

