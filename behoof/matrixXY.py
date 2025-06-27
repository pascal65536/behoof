import math


def create(size, fill="."):
    array = list()
    for _ in range(size):
        row = list()
        for _ in range(size):
            row.append(fill)
        array.append(row)
    return array


def show(matrix):
    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            print(matrix[row][col], end=" ")
        print()
    print("-" * len(matrix))


def copy(matrix):
    new_matrix = create(len(matrix))
    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            col1 = col
            row1 = row
            new_matrix[row1][col1] = matrix[row][col]
    return new_matrix


def flip_vertical(matrix):
    new_matrix = create(len(matrix))
    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            col1 = len(matrix[col]) - col - 1
            row1 = row
            new_matrix[row1][col1] = matrix[row][col]
    return new_matrix


def flip_horizontal(matrix):
    new_matrix = create(len(matrix))
    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            col1 = col
            row1 = len(matrix[row]) - row - 1
            new_matrix[row1][col1] = matrix[row][col]
    return new_matrix


def mirror(matrix):
    new_matrix = create(len(matrix))
    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            col1 = len(matrix[col]) - col - 1
            row1 = len(matrix[row]) - row - 1
            new_matrix[row1][col1] = matrix[row][col]
    return new_matrix


def flip_diagonal_main(matrix):
    new_matrix = create(len(matrix))
    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            col1 = row
            row1 = col
            new_matrix[row1][col1] = matrix[row][col]
    return new_matrix


def flip_diagonal_second(matrix):
    new_matrix = create(len(matrix))
    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            col1 = len(matrix[row]) - row - 1
            row1 = len(matrix[col]) - col - 1
            new_matrix[row1][col1] = matrix[row][col]
    return new_matrix


def rotate_ccw(matrix):
    new_matrix = create(len(matrix))
    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            col1 = row
            row1 = len(matrix[col]) - col - 1
            new_matrix[row1][col1] = matrix[row][col]
    return new_matrix


def rotate_cw(matrix):
    new_matrix = create(len(matrix))
    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            col1 = len(matrix[row]) - row - 1
            row1 = col
            new_matrix[row1][col1] = matrix[row][col]
    return new_matrix


# Matrix Calc

"""
Example for use Matrix calc

# Beginner set of coords
coords = [(0, 0), (1, 0), (1, 4), (2, 4), (2, 0), (3, 0), (3, 5), (0, 5), (0, 0)]
show(coords)

# Enlarge
base = base_create()
base = set_sx(base, 50, 50)
coords = get_new_coords(base, coords)

# Move
base = base_create()
base = set_tx(base, -100, 100)
coords = get_new_coords(base, coords)

# Rotate
base = base_create()
base = set_cx(base, 15)
coords = get_new_coords(base, coords)

show(coords)
"""


def base_create():
    base = create(3, fill=0)
    base[0][0] = 1
    base[1][1] = 1
    base[2][2] = 1
    return base


def matrix_calc(base, vector):
    x1 = base[0][0] * vector[0] + base[0][1] * vector[1] + base[0][2] * vector[2]
    y1 = base[1][0] * vector[0] + base[1][1] * vector[1] + base[1][2] * vector[2]
    z1 = base[2][0] * vector[0] + base[2][1] * vector[1] + base[2][2] * vector[2]
    return x1, y1, z1


def set_tx(base, tx, ty):
    "Перенос"
    base[0][2] = tx
    base[1][2] = ty
    return base


def set_sx(base, sx, sy):
    "Растяжение"
    base[0][0] = sx
    base[1][1] = sy
    return base


def set_cx(base, degrees):
    theta = math.radians(degrees)
    "Вращение относительно начала координат"
    base[0][0] = math.cos(theta)
    base[0][1] = -1 * math.sin(theta)
    base[1][1] = math.cos(theta)
    base[1][0] = math.sin(theta)
    return base


def get_new_coords(base, coords):
    new_coords = list()
    for coord in coords:
        vector = [coord[0], coord[1], 1]
        x1, y1, z1 = matrix_calc(base, vector)
        new_coords.append((x1, y1))
    return new_coords


if __name__ == "__main__":
    coords = [(0, 0), (1, 0), (1, 4), (2, 4), (2, 0), (3, 0), (3, 5), (0, 5), (0, 0)]
    show(coords)

    base = base_create()
    base = set_sx(base, 50, 50)
    coords = get_new_coords(base, coords)
    show(coords)

    base = base_create()
    base = set_tx(base, -100, 100)
    coords = get_new_coords(base, coords)
    show(coords)

    base = base_create()
    base = set_cx(base, 15)
    coords = get_new_coords(base, coords)
    show(coords)
