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


def is_prime(num):
    """
    Эта функция проверяет, является ли переданное число простым.
    """
    if num % 2 == 0:
        return False
    for i in range(3, int(num**0.5) + 1, 2):
        if num % i == 0:
            return False
    return True


def get_divisors(num):
    """
    Функция находит все делители заданного числа
    и возвращает их в виде множества
    """
    ret = {1, num}
    for i in range(2, num // 2 + 1):
        if num % i == 0:
            ret.add(i)
    return ret


def gcd(a, b):
    """
    Наибольший общий делитель.
    """
    return max(list(get_divisors(a) & get_divisors(b)))


def name_to_hex_color(name):
    """
    Функция вычисляет "цветовой никнейм"
    в формате шестнадцатичного цвета (HEX).
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


def generate_alternating_name(length):
    """
    Генерирует имя заданной длины, чередуя гласные и согласные буквы,
    начиная с гласной. Имя возвращается с заглавной буквы.
    """
    return "".join(
        random.choice(vowel if i % 2 == 0 else consonant) for i in range(length)
    ).capitalize()


def generate_fake_name(length=3):
    """
    Генерирует "фейковое" имя, состоящее из заданного количества слогов,
    где каждый слог состоит из согласной и гласной.
    Имя возвращается с заглавной буквы.
    """
    name = ""
    j = 0
    while j < length:
        name += random.choice(consonant)
        name += random.choice(vowel)
        j += 1
    return name.capitalize()


def load_json(folder_name, file_name):
    """
    Эта функция загружает данные из JSON-файла. Если указанный каталог
    не существует, она создает его. Если файл не существует,
    функция создает пустой JSON-файл. Затем она загружает
    и возвращает содержимое файла в виде словаря.
    """
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
    """
    Эта функция сохраняет словарь в формате JSON в указанный файл.
    Если указанный каталог не существует, она создает его.
    Затем она записывает переданный словарь в файл с заданным именем.
    """
    if not os.path.exists(folder_name):
        os.mkdir(folder_name)
    filename = os.path.join(folder_name, file_name)
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(save_dct, f, ensure_ascii=False, indent=4)


def upload_file(folder_name, uploaded_file, ext_lst=None):
    """
    Эта функция загружает файл в указанную папку, проверяет его расширение
    и создает уникальное имя для сохранения. Если папка не существует,
    она создается. Файл сохраняется в структуре папок на основе первых двух
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
        if string_1[i] != string_2[i]:
            distance += 1
    return distance


def cross(string_1, string_2):
    """
    Эта функция вычисляет коэффициент перекрестного сходства между двумя строками.
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


def generate_random_code_string():
    """
    Эта функция генерирует случайную строку, состоящую из букв латинского алфавита
    (как заглавных, так и строчных) и цифр. Она перемешивает символы и объединяет
    их в одну строку.
    """
    sad = list(string.ascii_letters + string.digits)
    random.shuffle(sad)
    return "".join(sad)


def logglog_message_to_csving(name, msg1, msg2, folder_name="log"):
    """
    Эта функция записывает сообщения в лог-файл в формате CSV.
    Она создает папку для логов (если она не существует), формирует имя файла
    на основе имени и добавляет в файл текущую дату и время, msg1 и msg2.
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


def calculate_md5(file_path):
    """
    Вычисляет MD5-хеш для файла
    """
    hash_md5 = hashlib.md5()
    with open(file_path, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()


def find_duplicate_files(folder):
    """
    Эта функция ищет дубликаты файлов в указанной папке.
    """
    files_dict = {}
    duplicates = []
    print(len(files_dict))
    for root, dirs, files in os.walk(folder):
        for file in files:
            file_path = os.path.join(root, file)
            file_hash = calculate_md5(file_path)
            if file_hash in files_dict:
                duplicates.append((file_path, files_dict[file_hash]))
            else:
                files_dict[file_hash] = file_path
    return duplicates


def delete_duplicate_files(duplicates):
    """
    Эта функция удаляет дубликаты файлов, переданные ей в виде списка.
    """
    ld = len(duplicates)
    for duplicate in duplicates:
        os.remove(duplicate[0])
        print(f"Removed duplicate file: {duplicate[0]}")
    print(ld)


def remove_empty_directories(root_folder):
    """
    Эта функция рекурсивно удаляет пустые папки в указанной корневой папке.
    """
    for folder_name in os.listdir(root_folder):
        folder_path = os.path.join(root_folder, folder_name)
        if os.path.isdir(folder_path):
            remove_empty_directories(folder_path)
            if not os.listdir(folder_path):
                print(f"Удаляется пустая папка: {folder_path}")
                os.rmdir(folder_path)


def move_file_to_folder_with_limit(file_source, folder_name, max_files_per_folder=100):
    """
    Эта функция перемещает файл из источника в папку,
    создавая подкаталоги по мере необходимости.
    Она проверяет, сколько файлов уже находится в каждом подкаталоге,
    и если количество файлов в текущем подкаталоге достигает
    максимального значения, создаёт новый подкаталог для перемещения файла.
    """
    os.makedirs(folder_name, exist_ok=True)
    maxfolder = 0
    for dirs in os.listdir(folder_name):
        local_dirs = os.path.join(folder_name, dirs)
        if os.path.isdir(local_dirs):
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
    print(f"Файл перемещен в {local_dirs}")


# def pifagor(a, b):
#     key = tuple(sorted([a, b]))
#     if key not in cache:
#         cache[key] = math.sqrt((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2)
#     return cache[key]


# def calc_vector(a, b):
#     ax, bx = a[0], b[0]
#     ay, by = a[1], b[1]
#     az, bz = a[2], b[2]
#     cat = math.sqrt((ax - bx) ** 2 + ((ay - by) ** 2) + (az - bz) ** 2)
#     return cat
