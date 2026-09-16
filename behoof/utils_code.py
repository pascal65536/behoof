"""
Утилитарный модуль: работа со строками, числами, файлами, хешами,
генерация имён, вычисление схожести текстов и т.п.
"""

import os
import re
import json
import uuid
import string
import shutil
import hashlib
import random
import datetime
import binascii
from collections import defaultdict, Counter
from math import log2

vowel = "aeiouy"  # гласные
consonant = "bcdfghjklmnpqrstvwxz"  # согласные
rus_alphabet = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"

transliteration = {
    "А": "A",
    "а": "a",
    "Б": "B",
    "б": "b",
    "В": "V",
    "в": "v",
    "Г": "G",
    "г": "g",
    "Д": "D",
    "д": "d",
    "Е": "E",
    "е": "e",
    "Ё": "E",
    "ё": "e",
    "Ж": "ZH",
    "ж": "zh",
    "З": "Z",
    "з": "z",
    "И": "I",
    "и": "i",
    "Й": "I",
    "й": "i",
    "К": "K",
    "к": "k",
    "Л": "L",
    "л": "l",
    "М": "M",
    "м": "m",
    "Н": "N",
    "н": "n",
    "О": "O",
    "о": "o",
    "П": "P",
    "п": "p",
    "Р": "R",
    "р": "r",
    "С": "S",
    "с": "s",
    "Т": "T",
    "т": "t",
    "У": "U",
    "у": "u",
    "Ф": "F",
    "ф": "f",
    "Х": "KH",
    "х": "kh",
    "Ц": "TC",
    "ц": "tc",
    "Ч": "CH",
    "ч": "ch",
    "Ш": "SH",
    "ш": "sh",
    "Щ": "SHCH",
    "щ": "shch",
    "Ы": "Y",
    "ы": "y",
    "Э": "E",
    "э": "e",
    "Ю": "IU",
    "ю": "iu",
    "Я": "IA",
    "я": "ia",
}


def is_palindrome(x):
    """
    Проверяет, является ли значение палиндромом.

    Значение сравнивается со своим разворотом. Поддерживаются строки,
    списки, кортежи и целые числа (число приводится к строке).

    Parameters
    ----------
    x : str or list or tuple or int
        Проверяемое значение.

    Returns
    -------
    bool
        True, если значение является палиндромом, иначе False.
    """
    if isinstance(x, str):
        xx = x
    elif isinstance(x, list):
        xx = x
    elif isinstance(x, tuple):
        xx = list(x)
    elif isinstance(x, int):
        xx = str(x)
    return xx[::-1] == xx


def is_prime(num: int) -> bool:
    """
    Проверяет, является ли число простым.

    Перебираются нечётные делители до sqrt(num). Числа < 2 простыми
    не считаются; 2 — простое.

    Parameters
    ----------
    num : int
        Проверяемое число.

    Returns
    -------
    bool
        True, если число простое, иначе False.
    """
    if num < 2:
        return False
    if num == 2:
        return True
    if num % 2 == 0:
        return False
    for i in range(3, int(num**0.5) + 1, 2):
        if num % i == 0:
            return False
    return True


def get_divisors(x):
    """
    Находит все делители заданного числа.

    Parameters
    ----------
    x : int
        Число, для которого ищутся делители.

    Returns
    -------
    list
        Отсортированный список всех делителей числа x.
    """
    dd = set()
    for d in range(1, int(x**0.5) + 1):
        if x % d == 0:
            dd.add(d)
            dd.add(x // d)
    return sorted(dd)


def gcd(a, b):
    """
    Находит наибольший общий делитель (НОД) двух чисел.

    Реализация через пересечение множеств делителей.

    Parameters
    ----------
    a : int
        Первое число.
    b : int
        Второе число.

    Returns
    -------
    int
        Наибольший общий делитель a и b.
    """
    return max(list(set(get_divisors(a)) & set(get_divisors(b))))


def lcm(a, b):
    """
    Находит наименьшее общее кратное (НОК) двух чисел.

    Parameters
    ----------
    a : int
        Первое число.
    b : int
        Второе число.

    Returns
    -------
    int
        Наименьшее общее кратное a и b.
    """
    return abs(a * b) // gcd(a, b)


def generate_name(telegram_id):
    """
    Генерирует псевдоним по telegram_id.

    Последние три цифры идентификатора используются как индексы
    для выбора цвета, прилагательного и животного.

    Parameters
    ----------
    telegram_id : int or str
        Идентификатор Telegram (как минимум 3 цифры).

    Returns
    -------
    str
        Строка вида "Красный Смешной Кот".
    """
    colors = [
        "Красный",
        "Синий",
        "Зеленый",
        "Желтый",
        "Фиолетовый",
        "Оранжевый",
        "Черный",
        "Белый",
        "Розовый",
        "Серый",
    ]
    adjectives = [
        "Смешной",
        "Сильный",
        "Умный",
        "Быстрый",
        "Мягкий",
        "Храбрый",
        "Тихий",
        "Яркий",
        "Доброжелательный",
        "Ласковый",
    ]
    animals = [
        "Кот",
        "Пёс",
        "Дельфин",
        "Заяц",
        "Лев",
        "Тигр",
        "Медведь",
        "Кролик",
        "Леопард",
        "Конь",
    ]
    telegram_str = str(telegram_id)
    return f"{colors[int(telegram_str[-3])]} {adjectives[int(telegram_str[-2])]} {animals[int(telegram_str[-1])]}"


def name_to_hex_color(name: str) -> str:
    """
    Генерирует hex-цвет из строки.

    Суммирует коды символов и переводит результат в шестнадцатеричную
    строку, дополняя её нулями до 6 символов.

    Parameters
    ----------
    name : str
        Строка, из которой генерируется цвет.

    Returns
    -------
    str
        Строка вида "#XXXXXX".
    """
    check_sum = 0
    for n in name:
        check_sum += ord(n)
    hexadecimal = ""
    hex_str = string.printable
    while check_sum // 16 > 0:
        hexadecimal = hex_str[check_sum % 16] + hexadecimal
        check_sum = check_sum // 16
    hexadecimal = hex_str[check_sum % 16] + hexadecimal
    hexadecimal = "#" + "0" * (6 - len(hexadecimal)) + hexadecimal
    return hexadecimal


def generate_alternating_name(length=5) -> str:
    """
    Генерирует имя заданной длины, чередуя гласные и согласные.

    Начинается с гласной. Первая буква — заглавная.

    Parameters
    ----------
    length : int, optional
        Длина имени (по умолчанию 5).

    Returns
    -------
    str
        Сгенерированное имя.
    """
    return "".join(
        random.choice(vowel if i % 2 == 0 else consonant) for i in range(length)
    ).capitalize()


def generate_fake_name(length=3) -> str:
    """
    Генерирует «фейковое» имя из заданного числа слогов.

    Каждый слог — согласная + гласная. Первая буква — заглавная.

    Parameters
    ----------
    length : int, optional
        Количество слогов (по умолчанию 3).

    Returns
    -------
    str
        Сгенерированное имя.
    """
    return "".join(
        f"{random.choice(consonant)}{random.choice(vowel)}" for _ in range(length)
    ).capitalize()


def hamming_distance(string_1, string_2):
    """
    Вычисляет расстояние Хэмминга между двумя строками.

    Сравниваются символы на одинаковых позициях до длины меньшей строки.

    Parameters
    ----------
    string_1 : str
        Первая строка.
    string_2 : str
        Вторая строка.

    Returns
    -------
    int
        Число различающихся позиций.
    """
    distance = 0
    for i in range(min(len(string_1), len(string_2))):
        if string_1[i] == string_2[i]:
            continue
        distance += 1
    return distance


def euclidean_distance(a: tuple, b: tuple) -> float:
    """
    Вычисляет евклидово расстояние между двумя точками на плоскости.

    Parameters
    ----------
    a : tuple
        Первая точка (x, y).
    b : tuple
        Вторая точка (x, y).

    Returns
    -------
    float
        Евклидово расстояние между точками.
    """
    return ((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2) ** 0.5


def generate_random_code_string():
    """
    Генерирует случайную строку из букв и цифр.

    Берётся набор ASCII-букв и цифр, перемешивается и склеивается
    в одну строку.

    Returns
    -------
    str
        Случайная буквенно-цифровая строка.
    """
    sad = list(string.ascii_letters + string.digits)
    random.shuffle(sad)
    return "".join(sad)


def clean_text(text):
    """
    Приводит текст к нижнему регистру и удаляет знаки препинания.

    Parameters
    ----------
    text : str
        Исходный текст.

    Returns
    -------
    str
        Очищенный текст.
    """
    text = text.lower()
    text = re.sub(r"[^\w\s]", "", text)
    return text


def generate_shingles(text, shingle_len=2):
    """
    Разбивает текст на шинглы (n-граммы) и считает их частоты.

    Каждое слово режется на подстроки длины shingle_len, каждая
    подстрока хэшируется через CRC32 и попадает в словарь частот.

    Parameters
    ----------
    text : str
        Исходный текст.
    shingle_len : int, optional
        Длина шингла (по умолчанию 2).

    Returns
    -------
    defaultdict
        Словарь {хэш_шингла: частота}.
    """
    words = text.split()
    shingles = []
    for word in words:
        i = 0
        while i < len(word):
            shingle = word[i : i + shingle_len]
            # Хэшируем шингл через CRC32 для компактного хранения
            shingle_hash = binascii.crc32(shingle.encode("utf-8"))
            shingles.append(shingle_hash)
            i += shingle_len
    shingles_dct = defaultdict(float)
    for sh in shingles:
        shingles_dct[sh] += 1.0
    return shingles_dct


# Similarity


def similarity(string_1: str, string_2: str) -> float:
    """
    Коэффициент схожести двух строк.

    Считается как отношение количества общих слов к общему числу слов
    (без знаков препинания, слова длиной > 2).

    Parameters
    ----------
    string_1 : str
        Первая строка.
    string_2 : str
        Вторая строка.

    Returns
    -------
    float
        Коэффициент схожести от 0 до 1.
    """
    t = str.maketrans("", "", string.punctuation)
    list_1 = {word.lower() for word in string_1.translate(t).split() if len(word) > 2}
    list_2 = {word.lower() for word in string_2.translate(t).split() if len(word) > 2}
    common_words = list_1.intersection(list_2)
    counter = len(common_words)
    total_length = len(list_1) + len(list_2)
    if total_length == 0:
        return 0
    return round(counter / total_length, 3)


def calculate_jaccard_similarity(str1, str2):
    """
    Вычисляет коэффициент Жаккара для двух строк.

    Строки очищаются от пунктуации и приводятся к нижнему регистру,
    затем сравниваются множества слов длиной > 2.

    Parameters
    ----------
    str1 : str
        Первая строка.
    str2 : str
        Вторая строка.

    Returns
    -------
    float
        Коэффициент Жаккара от 0 до 1.
    """
    str1 = str1.translate(str.maketrans("", "", string.punctuation)).lower()
    str2 = str2.translate(str.maketrans("", "", string.punctuation)).lower()
    words1 = set(word for word in str1.split() if len(word) > 2)
    words2 = set(word for word in str2.split() if len(word) > 2)
    intersection = words1.intersection(words2)
    union = words1.union(words2)
    if not union:
        return 0.0
    jaccard_index = len(intersection) / len(union)
    return round(jaccard_index, 3)


def weighted_jaccard(shingles1, shingles2):
    """
    Вычисляет взвешенный коэффициент Жаккара для словарей шинглов.

    Для каждого ключа берётся min и max из двух частот, затем
    суммируются по всем ключам.

    Parameters
    ----------
    shingles1 : dict
        Первый словарь {шингл: вес}.
    shingles2 : dict
        Второй словарь {шингл: вес}.

    Returns
    -------
    float
        Взвешенный коэффициент Жаккара.
    """
    keys = set(shingles1.keys()).union(shingles2.keys())
    min_sum = 0.0
    max_sum = 0.0
    for k in keys:
        w1 = shingles1.get(k, 0)
        w2 = shingles2.get(k, 0)
        min_sum += min(w1, w2)
        max_sum += max(w1, w2)
    if max_sum == 0:
        return 0.0
    return min_sum / max_sum


def calculate_entropy(data: bytes):
    """
    Вычисляет энтропию Шеннона для последовательности байт.

    Parameters
    ----------
    data : bytes
        Входные данные.

    Returns
    -------
    float
        Энтропия в битах. Для пустых данных возвращает 0.0.
    """
    if not data:
        return 0.0

    counts = Counter(data)
    size = len(data)
    return -sum((count / size) * log2(count / size) for count in counts.values())


def xor_data(data: bytes, key: bytes) -> bytes:
    """
    Применяет XOR-шифрование к данным с заданным ключом.

    Ключ циклически повторяется по всей длине данных.

    Parameters
    ----------
    data : bytes
        Входные данные.
    key : bytes
        Ключ шифрования.

    Returns
    -------
    bytes
        Результат побайтового XOR.
    """
    return bytes(value ^ key[i % len(key)] for i, value in enumerate(data))


# MD5


def calculate_md5(file_path: str) -> str:
    """
    Вычисляет MD5-хеш файла.

    Файл читается частями по 4 КБ, что позволяет обрабатывать
    большие файлы без загрузки в память.

    Parameters
    ----------
    file_path : str
        Путь к файлу.

    Returns
    -------
    str
        Hex-строка MD5-хеша.
    """
    hash_md5 = hashlib.md5()
    with open(file_path, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()


def str_to_md5(input_string):
    """
    Возвращает MD5-хеш UTF-8 строки.

    Parameters
    ----------
    input_string : str
        Входная строка.

    Returns
    -------
    str
        Hex-строка MD5-хеша.
    """
    hash_md5 = hashlib.md5(input_string.encode("utf-8"))
    return hash_md5.hexdigest()


# SHA256


def calculate_sha256(file_path: str) -> str:
    """
    Вычисляет SHA-256-хеш файла.

    Файл читается частями по 4 КБ, поэтому целиком в память
    не загружается — подходит и для больших файлов.

    Parameters
    ----------
    file_path : str
        Путь к файлу.

    Returns
    -------
    str
        Hex-строка SHA-256-хеша.
    """
    hash_sha256 = hashlib.sha256()

    with open(file_path, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_sha256.update(chunk)

    return hash_sha256.hexdigest()


def str_to_sha256(input_string: str) -> str:
    """
    Возвращает SHA-256-хеш UTF-8 строки.

    Parameters
    ----------
    input_string : str
        Входная строка.

    Returns
    -------
    str
        Hex-строка SHA-256-хеша.
    """
    hash_sha256 = hashlib.sha256(input_string.encode("utf-8"))
    return hash_sha256.hexdigest()


# Files


def logging_to_csv(name, msg1, msg2, folder_name="log") -> None:
    """
    Записывает сообщения в CSV-файл с меткой времени.

    В указанной папке (создаётся при необходимости) открывается
    файл name.csv в режиме добавления и туда пишется новая строка
    с текущим временем и двумя сообщениями.

    Parameters
    ----------
    name : str
        Имя CSV-файла (без расширения).
    msg1 : str
        Первое сообщение.
    msg2 : str
        Второе сообщение.
    folder_name : str, optional
        Папка для хранения CSV (по умолчанию "log").

    Returns
    -------
    None
    """
    if not os.path.exists(folder_name):
        os.mkdir(folder_name)
    file_name = f"{name}.csv"
    filename = os.path.join(folder_name, file_name)
    with open(filename, "a+", encoding="utf8", errors="replace", newline="") as f:
        x_lst = list()
        x_lst.append(datetime.datetime.now().isoformat())
        x_lst.append(msg1)
        x_lst.append(msg2)
        f.write(";".join([f'"{x}"' for x in x_lst]) + "\n")


def collect_files_lst(start_path: str) -> list:
    """
    Собирает полные пути ко всем файлам в каталоге и подкаталогах.

    Parameters
    ----------
    start_path : str
        Каталог, с которого начинается поиск.

    Returns
    -------
    list
        Список полных путей к найденным файлам.
    """
    file_path_lst = list()
    for root, _, files in os.walk(start_path):
        for file in files:
            file_path = os.path.join(root, file)
            file_path_lst.append(file_path)
    return file_path_lst


def moves_file(file_path: str, dst: str, category: str, folder_lst=list()) -> str:
    """
    Перемещает файл в каталог назначения с заданной категорией.

    Категория используется как последняя папка в пути назначения.
    Если файл с таким именем уже существует, к имени добавляется
    цифра «1» (до уникальности).

    Parameters
    ----------
    file_path : str
        Полный путь к перемещаемому файлу.
    dst : str
        Каталог назначения.
    category : str
        Имя категории (последняя папка).
    folder_lst : list, optional
        Промежуточные папки перед категорией.

    Returns
    -------
    str
        Полный путь к перемещённому файлу.
    """
    path = os.path.join(dst, *folder_lst, category)
    if not os.path.exists(path):
        os.makedirs(path)
    file_name = file_path.split("/")[-1]
    dst = os.path.join(path, file_name)
    while os.path.exists(dst):
        file_name = file_name.replace(".", "1.")
        dst = os.path.join(path, file_name)
    shutil.move(file_path, dst)
    return dst


def find_duplicate_files(folder: str) -> list:
    """
    Находит дубликаты файлов в каталоге.

    Обходит каталог и подкаталоги, считает MD5 каждого файла и
    сравнивает с уже встреченными.

    Parameters
    ----------
    folder : str
        Каталог для поиска.

    Returns
    -------
    list
        Список кортежей (путь_дубликата, путь_оригинала).
    """
    files_dict = {}
    duplicates = []
    for root, _, files in os.walk(folder):
        for file in files:
            file_path = os.path.join(root, file)
            file_hash = calculate_md5(file_path)
            if file_hash in files_dict:
                duplicates.append((file_path, files_dict[file_hash]))
            else:
                files_dict[file_hash] = file_path
    return duplicates


def delete_files(filelist: list) -> None:
    """
    Удаляет все файлы из списка.

    Parameters
    ----------
    filelist : list
        Список путей к файлам.

    Returns
    -------
    None
    """
    for filename in filelist:
        os.remove(filename)


def remove_empty_directories(root_folder: str) -> None:
    """
    Рекурсивно удаляет пустые каталоги.

    Parameters
    ----------
    root_folder : str
        Корневой каталог для очистки.

    Returns
    -------
    None
    """
    for folder_name in os.listdir(root_folder):
        folder_path = os.path.join(root_folder, folder_name)
        if not os.path.isdir(folder_path):
            continue
        remove_empty_directories(folder_path)
        if os.listdir(folder_path):
            continue
        os.rmdir(folder_path)


def move_file_to_folder_with_limit(file_source, folder_name, max_files_per_folder=100):
    """
    Перемещает файл в папку с ограничением на число файлов.

    Файл кладётся в подпапку с числовым именем. Если в текущей
    подпапке уже max_files_per_folder файлов, создаётся следующая.

    Parameters
    ----------
    file_source : str
        Путь к перемещаемому файлу.
    folder_name : str
        Имя папки-контейнера.
    max_files_per_folder : int, optional
        Максимум файлов в подпапке (по умолчанию 100).

    Returns
    -------
    None
    """
    os.makedirs(folder_name, exist_ok=True)
    maxfolder = 0
    for dirs in os.listdir(folder_name):
        local_dirs = os.path.join(folder_name, dirs)
        if not os.path.isdir(local_dirs):
            continue
        if dirs.isdigit() and maxfolder < int(dirs):
            maxfolder = int(dirs)
        lendir = len(os.listdir(local_dirs))
        if lendir < max_files_per_folder:
            break
    else:
        maxfolder += 1
        local_dirs = os.path.join(folder_name, str(maxfolder))
        os.makedirs(local_dirs, exist_ok=True)
    shutil.move(file_source, local_dirs)


def upload_file(folder_name, uploaded_file, ext_lst=None):
    """
    Сохраняет загруженный файл в каталоге с уникальным именем.

    Проверяет расширение, генерирует UUID-имя, создаёт подкаталоги
    по первым двум и следующим двум символам имени.

    Parameters
    ----------
    folder_name : str
        Корневая папка для сохранения.
    uploaded_file : file-like
        Объект с методами .read() и атрибутом .filename.
    ext_lst : list, optional
        Список разрешённых расширений. По умолчанию — изображения.

    Returns
    -------
    str or None
        Путь к сохранённому файлу или None, если расширение не разрешено.
    """
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


def load_json(folder_name_lst, file_name, default={}):
    """
    Загружает данные из JSON-файла, создавая каталог и файл при необходимости.

    Parameters
    ----------
    folder_name_lst : str or list
        Имя каталога (строка) или список его частей.
    file_name : str
        Имя JSON-файла.
    default : dict, optional
        Значение по умолчанию, если файл отсутствует.

    Returns
    -------
    dict
        Загруженный словарь.
    """
    if isinstance(folder_name_lst, str):
        folder_name = folder_name_lst
    elif isinstance(folder_name_lst, list):
        folder_name = os.path.join(*folder_name_lst)
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)
    filename = os.path.join(folder_name, file_name)
    if not os.path.exists(filename):
        with open(filename, "w", encoding="utf-8") as f:
            json.dump(default, f, ensure_ascii=True)
    with open(filename, encoding="utf-8") as f:
        load_dct = json.load(f)
    return load_dct


def save_json(folder_name_lst, file_name, save_dct):
    """
    Сохраняет словарь в JSON-файл, создавая каталог при необходимости.

    Parameters
    ----------
    folder_name_lst : str or list
        Имя каталога (строка) или список его частей.
    file_name : str
        Имя JSON-файла.
    save_dct : dict
        Сохраняемый словарь.

    Returns
    -------
    None
    """
    if isinstance(folder_name_lst, str):
        folder_name = folder_name_lst
    elif isinstance(folder_name_lst, list):
        folder_name = os.path.join(*folder_name_lst)
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)
    filename = os.path.join(folder_name, file_name)
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(save_dct, f, ensure_ascii=False, indent=4)


if __name__ == "__main__":
    pass
