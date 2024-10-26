DESCRIPTION = """
Copyright (C) 2020-2024 Sergey V. Pakhtusov (pascal65536@gmail.com)
Module for handling JSON data in Python.
"""

setupOpts = dict(
    name="pascal65536_utils",
    description="Module for handling JSON data in Python",
    long_description=DESCRIPTION,
    license="MIT",
    url="https://kompoblog.ru/",
    project_urls={
        "Documentation": "https://kompoblog.ru",
        "Source": "https://github.com/pascal65536/utils",
    },
    author="Sergey V. Pakhtusov",
    author_email="pascal65536@gmail.com",
    classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Development Status :: 2 - Beta",
        "Environment :: Other Environment",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Scientific/Engineering :: JSON data",
        "Topic :: Software Development :: Handling JSON data",
    ],
)


import os
import json
import uuid
import string
import shutil
import hashlib


from setuptools import find_namespace_packages, setup


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


def upload_file(folder_name, uploaded_file, ext_lst=None):
    if not ext_lst:
        ext_lst = ["jpg", "png", "gif", "jpeg", "webp"]
    uploaded_file_read = uploaded_file.read()
    filename = uploaded_file.filename
    ext = filename.split(".")[-1].lower()
    if ext not in ext_lst:
        return

    secret_filename = f"{uuid.uuid4()}.{ext}"
    folder = os.path.join(folder_name, secret_filename[:2], secret_filename[2:4])
    if not os.path.exists(folder):
        os.makedirs(folder)

    file_path = os.path.join(folder, secret_filename)
    with open(file_path, "wb") as f:
        f.write(uploaded_file_read)
    return file_path


def hamming_distance(string_1, string_2):
    """
    Расстояние Хэмминга
    """
    distance = 0
    for i in range(min(len(string_1), len(string_2))):
        if string_1[i] != string_2[i]:
            distance += 1
    return distance


def calculate_md5(file_path):
    """
    Вычисляет MD5-хеш для файла
    """
    hash_md5 = hashlib.md5()
    with open(file_path, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()


def cross(string_1, string_2):
    for ch in string.punctuation:
        string_1 = string_1.replace(ch, " ")
        string_2 = string_2.replace(ch, " ")
    string_1 = string_1.replace("  ", " ")
    string_2 = string_2.replace("  ", " ")

    list_1 = [word.lower() for word in string_1.split() if len(word) > 2]
    list_2 = [word.lower() for word in string_2.split() if len(word) > 2]

    counter = 0
    for word in list_2:
        if word in list_1:
            counter += 1

    for word in list_1:
        if word in list_2:
            counter += 1

    if len(list_1) + len(list_2) == 0:
        return 0

    return round(counter / (len(list_1) + len(list_2)), 3)


def collect_files_lst(start_path):
    """
    Обходит все папки и собирает ссылки на файлы в список
    """
    file_path_lst = list()
    for root, dirs, files in os.walk(start_path):
        for file in files:
            file_path = os.path.join(root, file)
            file_path_lst.append(file_path)
    return file_path_lst


def remove_book(key, book_path, base_folder=None, projects_folder=None):
    """
    Переместить по разным папкам
    """
    if not base_folder:
        base_folder = "base"
    if not projects_folder:
        projects_folder = "projects"
    path = os.path.join(base_folder, projects_folder, key)
    if not os.path.exists(path):
        os.makedirs(path)

    book_name = book_path.split("/")[-1]
    dst = os.path.join(path, book_name)
    while os.path.exists(dst):
        book_name = book_name.replace(".", "1.")
        dst = os.path.join(path, book_name)
    shutil.move(book_path, dst)
    return dst


setup(
    version="1.0.3",
    packages=find_namespace_packages(
        include=["pascal65536_utils", "pascal65536_utils.*"]
    ),
    python_requires=">=3.8",
    package_dir={"pascal65536_utils": "pascal65536_utils"},
    **setupOpts,
)
