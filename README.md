# Useful Utilities

```text
                           _  __  ____ ____ _____  __
 _ __   __ _ ___  ___ __ _| |/ /_| ___| ___|___ / / /_
| '_ \ / _` / __|/ __/ _` | | '_ \___ \___ \ |_ \| '_ \
| |_) | (_| \__ \ (_| (_| | | (_) |__) |__) |__) | (_) |
| .__/ \__,_|___/\___\__,_|_|\___/____/____/____/ \___/
|_|
```

> General-purpose utility library for Python.

[![PyPI](https://img.shields.io/pypi/v/behoof.svg)](https://pypi.org/project/behoof/)
[![Python](https://img.shields.io/pypi/pyversions/behoof.svg)](https://pypi.org/project/behoof/)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)

## About

**Useful Utilities** — универсальная библиотека вспомогательных функций
для Python.

Библиотека предоставляет инструменты для:

- работы со строками и текстом;
- математических вычислений;
- генерации тестовых данных;
- сравнения текстов;
- вычисления хэшей;
- анализа файлов;
- работы с JSON и CSV;
- управления файлами и каталогами;
- преобразования матриц и двумерных координат.

## Installation

```bash
pip install behoof
```

## Quick Start

```python
from behoof import (
    calculate_jaccard_similarity,
    is_prime,
)

print(is_prime(997))

result = calculate_jaccard_similarity(
    "Python is a powerful language",
    "Python is a popular language",
)

print(result)
```

Результат:

```text
True
0.5
```

## Library Map

| Раздел | Назначение |
|---|---|
| Strings | Работа со строками, алфавитами и именами |
| Mathematics | Простые числа, делители, НОД, НОК и расстояния |
| Similarity | Сравнение строк и текстов |
| Security | Энтропия, XOR и хэширование |
| Files | Поиск, перемещение и удаление файлов |
| Storage | Работа с JSON и CSV |
| Matrices | Преобразование двумерных матриц |

## Strings

### `is_palindrome`

Проверяет, является ли значение палиндромом.

Функция поддерживает:

- строки;
- списки;
- кортежи;
- целые числа.

#### Example

```python
from behoof import is_palindrome

print(is_palindrome("level"))
print(is_palindrome(12321))
print(is_palindrome("pascal65536"))
```

#### Output

```text
True
True
False
```

#### Signature

```python
is_palindrome(value) -> bool
```

### `generate_alternating_name`

Генерирует имя с чередованием гласных и согласных.

#### Example

```python
from behoof import generate_alternating_name

name = generate_alternating_name(6)

print(name)
```

Возможный результат:

```text
Inaker
```

Так как функция использует генератор случайных значений,
результат может отличаться при каждом запуске.

#### Signature

```python
generate_alternating_name(length=5) -> str
```

### `generate_fake_name`

Создает вымышленное имя из слогов вида:

```text
согласная + гласная
```

#### Example

```python
from behoof import generate_fake_name

print(generate_fake_name(3))
```

Возможный результат:

```text
Xerogo
```

#### Signature

```python
generate_fake_name(syllable_count=3) -> str
```

### `generate_name`

Создает имя на основе трех последних цифр идентификатора.

Цифры выбирают:

1. цвет;
2. прилагательное;
3. животное.

#### Example

```python
from behoof import generate_name

print(generate_name(123456789))
```

Результат:

```text
Белый Доброжелательный Конь
```

#### Signature

```python
generate_name(telegram_id) -> str
```

### `name_to_hex_color`

Преобразует строку в детерминированный цвет формата `#RRGGBB`.

Одинаковые строки возвращают одинаковый цвет.

#### Example

```python
from behoof import name_to_hex_color

print(name_to_hex_color("Pascal"))
```

Возможный результат:

```text
#000254
```

#### Signature

```python
name_to_hex_color(name) -> str
```

## Mathematics

### `is_prime`

Проверяет, является ли число простым.

#### Example

```python
from behoof import is_prime

numbers = [4, 17, 25, 97]

for number in numbers:
    print(number, is_prime(number))
```

Результат:

```text
4 False
17 True
25 False
97 True
```

#### Signature

```python
is_prime(number) -> bool
```

### `get_divisors`

Возвращает все положительные делители числа.

#### Example

```python
from behoof import get_divisors

print(get_divisors(36))
```

Результат:

```text
[1, 2, 3, 4, 6, 9, 12, 18, 36]
```

#### Signature

```python
get_divisors(number) -> list[int]
```

### `gcd`

Вычисляет наибольший общий делитель двух чисел.

#### Example

```python
from behoof import gcd

print(gcd(84, 30))
```

Результат:

```text
6
```

#### Signature

```python
gcd(first, second) -> int
```

### `lcm`

Вычисляет наименьшее общее кратное двух чисел.

#### Example

```python
from behoof import lcm

print(lcm(12, 18))
```

Результат:

```text
36
```

#### Signature

```python
lcm(first, second) -> int
```

### `euclidean_distance`

Вычисляет евклидово расстояние между двумя точками.

#### Example

```python
from behoof import euclidean_distance

point_a = (0, 0)
point_b = (3, 4)

print(euclidean_distance(point_a, point_b))
```

Результат:

```text
5.0
```

#### Signature

```python
euclidean_distance(first, second) -> float
```

## Text Similarity

### `hamming_distance`

Вычисляет расстояние Хэмминга между двумя строками.

#### Example

```python
from behoof import hamming_distance

print(hamming_distance("karolin", "kathrin"))
```

Результат:

```text
3
```

#### Signature

```python
hamming_distance(first, second) -> int
```

### `similarity`

Вычисляет простое сходство двух текстов
на основе общих уникальных слов.

#### Example

```python
from behoof import similarity

first = "Python is a powerful language"
second = "Python is a popular language"

print(similarity(first, second))
```

Результат:

```text
0.333
```

#### Signature

```python
similarity(first, second) -> float
```

### `calculate_jaccard_similarity`

Вычисляет коэффициент Жаккара для двух текстов.

Формула:

```text
J(A, B) = |A ∩ B| / |A ∪ B|
```

#### Example

```python
from behoof import calculate_jaccard_similarity

first = "python security automation"
second = "python security development"

result = calculate_jaccard_similarity(first, second)

print(result)
```

Результат:

```text
0.5
```

#### Signature

```python
calculate_jaccard_similarity(first, second) -> float
```

## Security and Hashing

### `calculate_entropy`

Вычисляет энтропию Шеннона для последовательности байтов.

Функция может использоваться для учебного анализа:

- текстовых файлов;
- архивов;
- зашифрованных данных;
- упакованных файлов.

#### Example

```python
from behoof import calculate_entropy

data = b"Python"

print(calculate_entropy(data))
```

Результат:

```text
2.584962500721156
```

> Высокая энтропия не доказывает наличие шифрования
> или вредоносного кода.

#### Signature

```python
calculate_entropy(data) -> float
```

### `xor_data`

Выполняет побитовую операцию XOR над данными и ключом.

#### Example

```python
from behoof import xor_data

message = b"hello"
key = b"key"

encrypted = xor_data(message, key)
decrypted = xor_data(encrypted, key)

print(encrypted)
print(decrypted)
```

Результат:

```text
b'\x03\x00\x15\x07\n'
b'hello'
```

> Это учебная функция. Повторяющийся XOR-ключ
> не является безопасным шифрованием.

#### Signature

```python
xor_data(data, key) -> bytes
```

### `calculate_sha256`

Вычисляет SHA-256-хэш файла.

#### Example

```python
from behoof import calculate_sha256

file_hash = calculate_sha256("example.bin")

print(file_hash)
```

Результат:

```text
e3b0c44298fc1c149afbf4c8996fb924...
```

#### Signature

```python
calculate_sha256(file_path) -> str
```

### `str_to_sha256`

Вычисляет SHA-256-хэш строки.

#### Example

```python
from behoof import str_to_sha256

print(str_to_sha256("hello world"))
```

Результат:

```text
b94d27b9934d3e08a52e52d7da7dabfa...
```

#### Signature

```python
str_to_sha256(value) -> str
```

## File Management

### `collect_files_lst`

Собирает список файлов в каталоге и его подкаталогах.

#### Example

```python
from behoof import collect_files_lst

files = collect_files_lst("./data")

for file_path in files:
    print(file_path)
```

Возможный результат:

```text
data/report.txt
data/images/photo.png
data/archive/data.zip
```

#### Signature

```python
collect_files_lst(start_path) -> list[str]
```

### `find_duplicate_files`

Ищет дубликаты файлов по хэшу.

#### Example

```python
from behoof import find_duplicate_files

duplicates = find_duplicate_files("./data")

for duplicate, original in duplicates:
    print(f"{duplicate} == {original}")
```

Возможный результат:

```text
data/copy.txt == data/original.txt
data/photo_2.png == data/photo.png
```

#### Signature

```python
find_duplicate_files(folder) -> list[tuple[str, str]]
```

### `delete_files`

Удаляет файлы из переданного списка.

#### Example

```python
from behoof import delete_files

delete_files([
    "temporary/file_1.tmp",
    "temporary/file_2.tmp",
])
```

#### Signature

```python
delete_files(filelist) -> None
```

### `remove_empty_directories`

Удаляет пустые каталоги.

#### Example

```python
from behoof import remove_empty_directories

remove_empty_directories("./data")
```

#### Signature

```python
remove_empty_directories(root_folder) -> None
```

## JSON and CSV

### `load_json`

Загружает данные из JSON-файла.

Если каталог или файл отсутствуют,
они создаются автоматически.

#### Example

```python
from behoof import load_json

settings = load_json(
    folder_name_lst=["data", "config"],
    file_name="settings.json",
    default={
        "debug": False,
        "language": "ru",
    },
)

print(settings)
```

Результат:

```python
{
    "debug": False,
    "language": "ru",
}
```

#### Signature

```python
load_json(
    folder_name_lst,
    file_name,
    default=None,
) -> Any
```

### `save_json`

Сохраняет данные в JSON-файл.

#### Example

```python
from behoof import save_json

save_json(
    folder_name_lst=["data", "config"],
    file_name="settings.json",
    save_dct={
        "debug": True,
        "language": "ru",
    },
)
```

Содержимое файла:

```json
{
    "debug": true,
    "language": "ru"
}
```

#### Signature

```python
save_json(
    folder_name_lst,
    file_name,
    save_dct,
) -> None
```

### `logging_to_csv`

Добавляет запись в CSV-файл вместе с временной меткой.

#### Example

```python
from behoof import logging_to_csv

logging_to_csv(
    name="application",
    msg1="User login",
    msg2="Authentication successful",
)
```

Создается файл:

```text
log/application.csv
```

#### Signature

```python
logging_to_csv(
    name,
    msg1,
    msg2,
    folder_name="log",
) -> None
```

## Matrix Operations

Матричный модуль предназначен для преобразования
двумерных структур.

Он может использоваться в:

- компьютерной графике;
- обработке изображений;
- играх;
- геометрических расчетах;
- моделировании двумерного пространства.

### `create`

Создает матрицу заданного размера.

#### Example

```python
from behoof.matrix import create

matrix = create(3, 0)

print(matrix)
```

Результат:

```text
[[0, 0, 0], [0, 0, 0], [0, 0, 0]]
```

### `rotate_cw`

Поворачивает матрицу на 90 градусов
по часовой стрелке.

#### Example

```python
from behoof.matrix import rotate_cw

matrix = [[0, 1, 0], [0, 2, 0], [0, 3, 0]]

print(rotate_cw(matrix))
```

Результат:

```text
[[0, 0, 0], [3, 2, 1], [0, 0, 0]]
```

### `rotate_ccw`

Поворачивает матрицу на 90 градусов
против часовой стрелки.

#### Example

```python
from behoof.matrix import rotate_ccw

matrix = [[0, 1, 0], [0, 2, 0], [0, 3, 0]]

print(rotate_ccw(matrix))
```

Результат:

```text
[[0, 0, 0], [1, 2, 3], [0, 0, 0]]
```

### `flip_horizontal`

Отражает матрицу по горизонтали.

#### Example

```python
from behoof.matrix import flip_horizontal

matrix = [[0, 1, 0], [0, 2, 0], [0, 3, 0]]

print(flip_horizontal(matrix))
```

Результат:

```text
[[0, 3, 0], [0, 2, 0], [0, 1, 0]]
```

### `flip_vertical`

Отражает матрицу по вертикали.

#### Example

```python
from behoof.matrix import flip_vertical

matrix = [[0, 1, 9], [0, 2, 0], [6, 3, 0]]

print(flip_vertical(matrix))
```

Результат:

```text
[[9, 1, 0], [0, 2, 0], [0, 3, 6]]
```

### `flip_diagonal_main`

Отражает матрицу относительно главной диагонали.

#### Example

```python
from behoof.matrix import flip_diagonal_main

matrix = [[0, 1, 9], [0, 2, 0], [6, 3, 0]]

print(flip_diagonal_main(matrix))
```

Результат:

```text
[[0, 0, 6], [1, 2, 3], [9, 0, 0]]
```

### `flip_diagonal_second`

Отражает матрицу относительно побочной диагонали.

#### Example

```python
from behoof.matrix import flip_diagonal_second

matrix = [[0, 1, 9], [0, 2, 0], [6, 3, 0]]

print(flip_diagonal_second(matrix))
```

Результат:

```text
[[0, 0, 9], [3, 2, 1], [6, 0, 0]]
```

### `mirror`

Создает зеркальное отражение матрицы.

#### Example

```python
from behoof.matrix import mirror

matrix = [[0, 1, 9], [0, 2, 0], [6, 3, 0]]

print(mirror(matrix))
```

Результат:

```text
[[0, 3, 6], [0, 2, 0], [9, 1, 0]]
```

### `show`

Выводит матрицу в удобном формате.

#### Example

```python
from behoof.matrix import show

matrix = [[0, 1, 9], [0, 2, 0], [6, 3, 0]]

show(matrix)
```

Результат:

```text
0 1 9 
0 2 0 
6 3 0 
---
```

## Coordinate Transformations

Функции `set_cx`, `set_sx`, `set_tx` предназначены для преобразований двумерного пространства.

Они могут использоваться в:

- компьютерной графике;
- обработке изображений;
- геометрических расчетах;
- игровых движках;
- моделировании объектов.

### Растяжение

```python
coords = [(0, 0), (1, 0), (1, 4), (2, 4), (2, 0), (3, 0), (3, 5), (0, 5), (0, 0)]
show(coords)

base = base_create()
base = set_sx(base, 50, 50)  # Растянуть фигуру по x на 50 и по y на 50
coords = get_new_coords(base, coords)
show(coords)
```

Результат:

```text
0 0 
1 0 
1 4 
2 4 
2 0 
3 0 
3 5 
0 5 
0 0 
---------
0 0 
50 0 
50 200 
100 200 
100 0 
150 0 
150 250 
0 250 
0 0 
---------
```

### Перенос

```python
coords = [(0, 0), (1, 0), (1, 4), (2, 4), (2, 0), (3, 0), (3, 5), (0, 5), (0, 0)]
show(coords)

base = base_create()
base = set_tx(base, -100, 100)  # Перенести фигуру на новые координаты (-100, 100)
coords = get_new_coords(base, coords)
show(coords)
```

Результат:

```text
0 0 
1 0 
1 4 
2 4 
2 0 
3 0 
3 5 
0 5 
0 0 
---------
-100 100 
-99 100 
-99 104 
-98 104 
-98 100 
-97 100 
-97 105 
-100 105 
-100 100 
---------
```

### Вращение относительно начала координат

```python
coords = [(0, 0), (1, 0), (1, 4), (2, 4), (2, 0), (3, 0), (3, 5), (0, 5), (0, 0)]
show(coords)

base = base_create()
base = set_cx(base, 15)  # Повернуть фигуру на 15 градусов
coords = get_new_coords(base, coords)
show(coords)
```

Результат:

```text
0 0 
1 0 
1 4 
2 4 
2 0 
3 0 
3 5 
0 5 
0 0 
---------
0.0 0.0 
0.9659258262890683 0.25881904510252074 
-0.06935035412101465 4.122522350258794 
0.8965754721680537 4.381341395361314 
1.9318516525781366 0.5176380902050415 
2.897777478867205 0.7764571353075622 
1.6036822533546014 5.606086266752904 
-1.2940952255126037 4.8296291314453415 
0.0 0.0 
---------
```
