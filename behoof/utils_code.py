import os
import json
import uuid
import string
import shutil
import hashlib
import random
import datetime


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
    Checks if the given value is a palindrome.

    The function checks if the given value is equal to its reverse.
    It works with strings, lists, tuples and integers.

    Parameters
    ----------
    x : str or list or tuple or int
        The value to check.

    Returns
    -------
    bool
        True if the value is a palindrome, False otherwise.
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
    Checks if the given number is prime.

    The function works by checking divisibility of the given number
    by all odd numbers up to the square root of the given number.
    If the number is divisible by any of these, it is not prime.
    Otherwise, it is prime.

    Parameters
    ----------
    num : int
        The number to check.

    Returns
    -------
    bool
        True if the number is prime, False otherwise.
    """
    if num % 2 == 0:
        return False
    for i in range(3, int(num**0.5) + 1, 2):
        if num % i == 0:
            return False
    return True


def get_divisors(x):
    """
    Функция находит все делители заданного числа
    и возвращает их в виде множества
    """
    dd = set()
    for d in range(1, int(x**0.5) + 1):
        if x % d == 0:
            dd.add(d)
            dd.add(x // d)
    return sorted(dd)


def gcd(a, b):
    """
    Функция находит Наибольший общий делитель (НОД).
    """
    return max(list(get_divisors(a) & get_divisors(b)))


def lcm(a, b):
    """
    Функция находит Наименьшее общее кратное (НОК).
    """
    return abs(a * b) // gcd(a, b)


def generate_name(telegram_id):
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
    This function generates a hex color from a given name by summing
    up the ordinal values of the characters in the name and converting
    the result to a hexadecimal string. The string is then prefixed with
    "#" and padded with zeros to a length of 6 characters.

    Parameters
    ----------
    name : str
        The string to generate the color from.

    Returns
    -------
    str
        A hex color string in the format "#XXXXXX".
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
    Функция генерирует имя заданной длины, чередуя гласные
    и согласные буквы, начиная с гласной. Имя возвращается
    с заглавной буквы.
    """
    return "".join(
        random.choice(vowel if i % 2 == 0 else consonant) for i in range(length)
    ).capitalize()


def generate_fake_name(length=3) -> str:
    """
    Функция генерирует "фейковое" имя, состоящее из заданного
    количества слогов, где каждый слог состоит из согласной
    и гласной. Имя возвращается с заглавной буквы.
    """
    return "".join(
        f"{random.choice(consonant)}{random.choice(vowel)}" for _ in range(length)
    ).capitalize()


def load_json(folder_name_lst, file_name, default={}):
    """
    Функция загружает данные из JSON-файла. Если указанный каталог
    не существует, она создает его. Если файл не существует,
    функция создает пустой JSON-файл. Затем она загружает
    и возвращает содержимое файла в виде словаря.
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
    Функция сохраняет словарь в формате JSON в указанный файл.
    Если указанный каталог не существует, она создает его.
    Затем она записывает переданный словарь в файл с заданным именем.
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


def upload_file(folder_name, uploaded_file, ext_lst=None):
    """
    Функция загружает файл в указанную папку,
    проверяет его расширение
    и создает уникальное имя для сохранения.
    Если папка не существует, она создается.
    Файл сохраняется в структуре папок на основе первых двух
    символов уникального имени файла.
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


def hamming_distance(string_1, string_2):
    """
    Расстояние Хэмминга
    """
    distance = 0
    for i in range(min(len(string_1), len(string_2))):
        if string_1[i] == string_2[i]:
            continue
        distance += 1
    return distance


def similarity(string_1: str, string_2: str) -> float:
    """
    Coefficient of similarity between two strings, calculated as a ratio of common words to total number of words.

    :param string_1: first string
    :param string_2: second string
    :return: coefficient of similarity (0 - 1)
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
    Вычисляет коэффициент Жаккара
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


def collect_files_lst(start_path: str) -> list:
    """
    Collects a list of full paths to all files in the given directory and its subdirectories.

    :param start_path: the directory to start searching from
    :return: a list of full paths to all files found
    """
    file_path_lst = list()
    for root, _, files in os.walk(start_path):
        for file in files:
            file_path = os.path.join(root, file)
            file_path_lst.append(file_path)
    return file_path_lst


def moves_file(file_path: str, dst: str, category: str, folder_lst=list()) -> str:
    """
    Moves a file to a specified destination directory with a given category name.

    The given category name will be used as the last folder in the destination path.
    If the given category name already exists in the destination directory, the file
    will be moved to a subfolder of the category with the same name, but with a number
    appended to the end (starting from 1).

    :param file_path: the full path to the file to move
    :param dst: the destination directory
    :param category: the category name to use for the last folder in the destination path
    :param folder_lst: a list of folder names to use before the category name
    :return: the full path to the moved file
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


def generate_random_code_string():
    """
    Generates a random string of alphanumeric characters.

    This function shuffles the string containing all upper and lower case
    letters of the alphabet and all digits, and then joins them together into
    a single string. The length of the string is equal to the number of all
    possible alphanumeric characters.

    Returns
    -------
    string
        A random alphanumeric string.
    """
    sad = list(string.ascii_letters + string.digits)
    random.shuffle(sad)
    return "".join(sad)


def logging_to_csv(name, msg1, msg2, folder_name="log") -> None:
    """
    Logs messages to a CSV file with a timestamp.

    This function appends a new line to a CSV file in the specified folder,
    containing the current timestamp and the provided messages.

    Parameters
    ----------
    name : str
        The base name of the CSV file (without extension).
    msg1 : str
        The first message to log.
    msg2 : str
        The second message to log.
    folder_name : str, optional
        The name of the folder where the CSV file is stored (default is "log").
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


def log_action(func):
    '''Декоратор для логирования'''

    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            # Логируем входные параметры
            logging.info(f'Calling function: {func.__name__} with args: {args[0].json} and kwargs: {kwargs}')
            result = func(*args, **kwargs)
            # Логируем выходное значение
            logging.info(f'Function {func.__name__} returned: {result}')
            return result
        except Exception as e:
            # Логируем исключения
            logging.error(f'Exception in function {func.__name__}: {e}', exc_info=True)
            raise
    return wrapper


def calculate_md5(file_path: str) -> str:
    """
    This function calculates the MD5 hash of the given file.
    It reads the file in 4KB chunks and updates the MD5 hash
    with each chunk. This way it can handle large files without
    loading the whole file into memory.
    """
    hash_md5 = hashlib.md5()
    with open(file_path, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()


def str_to_md5(input_string):
    hash_md5 = hashlib.md5(input_string.encode("utf-8"))
    return hash_md5.hexdigest()


def find_duplicate_files(folder: str) -> list:
    """
    Finds duplicate files in the given folder.

    This function walks through the given folder and its subfolders, and
    calculates the MD5 hash of each file. It then checks if a file with the
    same hash already exists in the dictionary. If it does, it adds the file
    path to the list of duplicates. If not, it adds the file path to the
    dictionary with the hash as the key. Finally, it returns the list of
    duplicates.

    :param folder: the folder to search for duplicates in
    :return: a list of tuples, where each tuple contains two file paths that
             are duplicates of each other
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
    Deletes all files in the given list.

    :param filelist: a list of file paths to delete
    """
    ld = len(filelist)
    for filename in filelist:
        os.remove(filename)


def remove_empty_directories(root_folder: str) -> None:
    """
    Recursively removes empty directories from the given root folder.

    :param root_folder: path to the root folder to start from
    :return: None
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
    Moves the given file to a folder with the given name.

    The folder will be created if it does not exist.
    The file will be moved to a subfolder of the given folder, with a name that is
    the next number in sequence (starting from 0). The subfolder will be created
    if it does not exist.
    If the number of files in the current subfolder is less than max_files_per_folder,
    the file will be moved to that subfolder. Otherwise, a new subfolder will be created.

    :param file_source: the path to the file to move
    :param folder_name: the name of the folder to move the file to
    :param max_files_per_folder: the maximum number of files to store in each subfolder
    :return: None
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


def euclidean_distance(a: tuple, b: tuple) -> float:
    """
    Calculates the Euclidean distance between two points given as tuples of two
    numbers (e.g. (x, y)).

    Parameters
    ----------
    a : tuple
        The first point.
    b : tuple
        The second point.

    Returns
    -------
    float
        The Euclidean distance between the two points.
    """
    return ((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2) ** 0.5


if __name__ == "__main__":
    pass
