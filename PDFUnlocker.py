import importlib
import sys

REQUIRED_MODULES = ['tkinter', 'PyPDF2', 'os', 'time', 'itertools']

for module in REQUIRED_MODULES:
    try:
        importlib.import_module(module)
    except ImportError:
        print(f"必要なライブラリ '{module}' が見つかりません。以下のコマンドでインストールしてください:\n")
        print(f"pip install {module}\n")
        sys.exit()
        

import tkinter as tk
from tkinter import filedialog
from PyPDF2 import PdfReader, PdfWriter
import os
import time
import itertools

print("PDFファイルのパスワードを解析します")
print("このコードを使用する際は、必ず法律と倫理を遵守してください")

PASSWORD_DISPLAY_INTERVAL = 100  # パスワード表示の間隔

def unlock_pdf(file_path, output_path, start, end, include_uppercase=False):
    with open(file_path, 'rb') as pdf_file:
        pdf_reader = PdfReader(pdf_file)

        if pdf_reader.is_encrypted:
            start_time = time.time()

            for i in range(start, end):
                password_found = try_passwords(pdf_reader, i, output_path, include_uppercase)
                if password_found:
                    end_time = time.time()
                    print("復号化されたPDFが保存されました {}".format(output_path))
                    print("パスワード解除にかかった時間: {}秒".format(end_time - start_time))
                    return

            print("適切なパスワードが見つかりませんでした")
        else:
            print("PDFファイルは暗号化されていません")

def try_passwords(pdf_reader, length, output_path, include_uppercase):
    for idx, password in enumerate(generate_passwords(length, include_uppercase)):
        if idx % PASSWORD_DISPLAY_INTERVAL == 0:
            print("現在試行しているパスワード: ", password)

        try:
            pdf_reader.decrypt(password)

            pdf_writer = PdfWriter()

            for page in pdf_reader.pages:
                pdf_writer.add_page(page)

            with open(output_path, 'wb') as output_pdf:
                pdf_writer.write(output_pdf)

            print("成功したパスワード: ", password)  # 正しいパスワードを表示
            return True
        except:
            continue

    return False

def generate_passwords(length, include_uppercase=False):
    charset = '0123456789abcdefghijklmnopqrstuvwxyz'
    if include_uppercase:
        charset += 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
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
        include_uppercase = input("パスワード解析に英大文字を含めますか？Nを選択すると半角英数小文字のみで解析します (Y/N): ").upper() == "Y"
        unlock_pdf(pdf_file_path, save_path, 1, 9, include_uppercase)
    else:
        print("選択したファイルが存在しません")
