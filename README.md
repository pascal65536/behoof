Useful utilities

Copyright (C) 2020-2025 Sergey V. Pakhtusov aka pascal65536

```
                           _  __  ____ ____ _____  __   
 _ __   __ _ ___  ___ __ _| |/ /_| ___| ___|___ / / /_  
| '_ \ / _` / __|/ __/ _` | | '_ \___ \___ \ |_ \| '_ \ 
| |_) | (_| \__ \ (_| (_| | | (_) |__) |__) |__) | (_) |
| .__/ \__,_|___/\___\__,_|_|\___/____/____/____/ \___/ 
|_|                                                     

```

A general-purpose utility library offering a wide range of functions

`pip install behoof`

This Python project to be a versatile utility library offering a wide range of functionalities, including:

1. String and Text Manipulation:

   - vowel, consonant, rus_alphabet, transliteration, is_palindrome - Functions related to character analysis, alphabet manipulation, and palindrome detection.

   - generate_alternating_name, generate_fake_name - Functions for generating names, potentially for testing or data generation purposes.

2. Mathematical Operations:

   - is_prime, get_divisors, gcd, lcm - Functions for prime number detection, divisor finding, and calculation of greatest common divisor and least common multiple.

   - euclidean_distance - Functions for calculates the Euclidean distance between two points given as tuples of two numbers (e.g. (x, y)).

3. Data Handling and I/O:

   - generate_name, name_to_hex_color, load_json, save_json, upload_file - Functions for color generation, JSON file handling, and file uploading.

   - log_action, logging_to_csv - Function for logging messages to a CSV file.

4. Text Similarity and Distance:

   - hamming_distance, similarity, calculate_jaccard_similarity - Functions for calculating text similarity and distance metrics.

5. File Management and Manipulation:

   - collect_files_lst, moves_file, generate_random_code_string - Functions for collecting files, moving files, and generating random code strings.

   - calculate_md5, find_duplicate_files, delete_files, remove_empty_directories, move_file_to_folder_with_limit - Functions specifically focused on duplicate file management, including MD5 hashing, duplicate file detection, deletion, and organization into folders with limited file counts.

6. Working with matrices. Matrix transformation of 2D space.
 
   - rotate_ccw, rotate_cw, copy, create, flip_diagonal_main, flip_diagonal_second, flip_horizontal, flip_vertical, mirror, show

   - set_cx, set_sx, set_tx, base_create, get_new_coords matrix_calc