puzzle_input_file = open('input.txt', 'r')
puzzle_input = puzzle_input_file.read()

lines = puzzle_input.split('\n')

height = len(lines)
width = len(lines[0])

sum = 0

parts = {}


def has_adjacent(start, size, y):
    right_limit = start + size
    if start > 0:
        x, found_y = start - 1, -1

        if is_left_neighbor(start, y):
            found_y = y
        elif is_left_top_diagonal(start, y):
            found_y = y - 1
        elif is_left_bottom_diagonal(start, y):
            found_y = y + 1

        if found_y != -1:
            return True, x, found_y

    if right_limit < width - 1:
        x, found_y = right_limit, -1

        if is_right_neighbor(y, right_limit):
            found_y = y
        elif is_right_bottom_diagonal(y, right_limit):
            found_y = y + 1
        elif is_right_top_diagonal(y, right_limit):
            found_y = y - 1

        if found_y != -1:
            return True, x, found_y

    if y > 0:
        for i in range(start, right_limit):
            if not lines[y - 1][i].isnumeric() and lines[y - 1][i] == '*':
                return True, i, y-1

    if y < height - 1:
        for i in range(start, right_limit):
            if lines[y + 1][i] == '*':
                return True, i, y+1

    return (False, -1, -1)


def is_right_top_diagonal(y, right_limit):
    return y > 0 and lines[y - 1][right_limit] == '*'


def is_right_bottom_diagonal(y, right_limit):
    return y < height - 1 and lines[y + 1][right_limit] == '*'


def is_right_neighbor(y, right_limit):
    return lines[y][right_limit] == '*'


def is_left_bottom_diagonal(start, y):
    return y < height - 1 and lines[y + 1][start - 1] == '*'


def is_left_top_diagonal(start, y):
    return y > 0 and lines[y - 1][start - 1] == '*'


def is_left_neighbor(start, y):
    return lines[y][start - 1] == '*'


accumulator = ''
start = -1
size = 0

for y in range(height):
    if accumulator != '':
        is_adjacenct, found_x, found_y = has_adjacent(start, size, y)
        if is_adjacenct:
            id = f'{found_x}_{found_y}'
            if not id in parts:
                parts[id] = []
            parts[id].append(int(accumulator))

        accumulator = ''
        start = -1
        size = 0

    for x in range(width):
        char = lines[y][x]
        if char.isnumeric():
            if start < 0:
                start = x

            accumulator += char
            size += 1
        elif accumulator != '':
            is_adjacenct, found_x, found_y = has_adjacent(start, size, y)
            if is_adjacenct:
                id = f'{found_x}_{found_y}'
                if not id in parts:
                    parts[id] = []
                parts[id].append(int(accumulator))

            accumulator = ''
            start = -1
            size = 0


for part_coord in parts:
    if len(parts[part_coord]) == 2:
        ratio = parts[part_coord][0] * parts[part_coord][1]
        sum += ratio

print(sum)
