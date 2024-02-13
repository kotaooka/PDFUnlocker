import tkinter as tk
from tkinter import filedialog
from PyPDF2 import PdfReader, PdfWriter
import os
import time
import itertools

print("このコードを使用する際は、必ず法律と倫理を遵守してください")

def unlock_pdf(file_path, output_path, start, end):
    with open(file_path, 'rb') as pdf_file:
        pdf_reader = PdfReader(pdf_file)

        if pdf_reader.is_encrypted:
            start_time = time.time()

            for i in range(start, end):
                password_found = try_passwords(pdf_reader, i, output_path)
                if password_found:
                    end_time = time.time()
                    print("復号化されたPDFが保存されました {}".format(output_path))
                    print("パスワード解除にかかった時間: {}秒".format(end_time - start_time))
                    return

            print("適切なパスワードが見つかりませんでした")
        else:
            print("PDFファイルは暗号化されていません")

def try_passwords(pdf_reader, length, output_path):
    for password in generate_passwords(length):
        print("現在試行しているパスワード: ", password)

        try:
            pdf_reader.decrypt(password)

            pdf_writer = PdfWriter()

            for page in pdf_reader.pages:
                pdf_writer.add_page(page)

            with open(output_path, 'wb') as output_pdf:
                pdf_writer.write(output_pdf)

            return True
        except:
            continue

    return False

def generate_passwords(length):
    charset = '0123456789abcdefghijklmnopqrstuvwxyz'
    for password in itertools.product(charset, repeat=length):
        yield ''.join(password)

def select_pdf_files():
    root = tk.Tk()
    root.withdraw() 
    file_paths = filedialog.askopenfilenames(initialdir="C:/", filetypes=[("PDF files", "*.pdf")])  # ファイルダイアログを開く
    return file_paths

pdf_file_paths = select_pdf_files()

for pdf_file_path in pdf_file_paths:
    if os.path.isfile(pdf_file_path):
        save_path = os.path.join(os.path.dirname(pdf_file_path), "decrypted_" + os.path.basename(pdf_file_path))
        unlock_pdf(pdf_file_path, save_path, 1, 9)
    else:
        print("選択したファイルが存在しません")
