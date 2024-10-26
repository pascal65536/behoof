#.  Copyright (C) 2020-2024   Sergey V. Pakhtusov (pascal65536@gmail.com)
#  Module for handling JSON data in Python.
#


import os
import json
import uuid


def load_json(folder_name, file_name):
    if not os.path.exists(folder_name):
        os.mkdir(folder_name)
    filename = os.path.join(folder_name, file_name)
    if not os.path.exists(filename):
        with open(filename, "w", encoding="utf-8") as f:
            json.dump(dict(), f, ensure_ascii=True)
    with open(filename, encoding="utf-8") as f:
        load_dct = json.load(f)
    return load_dct


def save_json(folder_name, file_name, save_dct):
    if not os.path.exists(folder_name):
        os.mkdir(folder_name)
    filename = os.path.join(folder_name, file_name)
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(save_dct, f, ensure_ascii=False, indent=4)


def upload_file(folder_name, uploaded_file):
    uploaded_file_read = uploaded_file.read()
    filename = uploaded_file.filename
    ext = filename.split(".")[-1].lower()
    if ext not in ["jpg", "png", "gif", "jpeg", "webp"]:
        return 

    secret_filename = f"{uuid.uuid4()}.{ext}"    
    folder = os.path.join(folder_name, secret_filename[:2], secret_filename[2:4])
    if not os.path.exists(folder):
        os.makedirs(folder)

    file_path = os.path.join(folder, secret_filename)
    with open(file_path, "wb") as f:
        f.write(uploaded_file_read)
    
    return file_path
