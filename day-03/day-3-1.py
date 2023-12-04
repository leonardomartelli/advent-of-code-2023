puzzle_input_file = open('input.txt', 'r')
puzzle_input = puzzle_input_file.read()

lines = puzzle_input.split('\n')

height = len(lines)
width = len(lines[0])

sum = 0


def has_adjacent(start, size, y):
    right_limit = start + size
    if start > 0 and (is_left_neighbor(start, y) or is_left_top_diagonal(start, y) or is_left_bottom_diagonal(start, y)):
        return True
    elif right_limit < width - 1 and (is_right_neighbor(y, right_limit) or is_right_bottom_diagonal(y, right_limit) or is_right_top_diagonal(y, right_limit)):
        return True
    elif y > 0:
        for i in range(start, right_limit):
            if not lines[y - 1][i].isnumeric() and lines[y - 1][i] != '.':
                return True
    if y < height - 1:
        for i in range(start, right_limit):
            if not lines[y + 1][i].isnumeric() and lines[y + 1][i] != '.':
                return True
    return False


def is_right_top_diagonal(y, right_limit):
    return y > 0 and not lines[y - 1][right_limit].isnumeric() and lines[y - 1][right_limit] != '.'


def is_right_bottom_diagonal(y, right_limit):
    return y < height - 1 and not lines[y + 1][right_limit].isnumeric() and lines[y + 1][right_limit] != '.'


def is_right_neighbor(y, right_limit):
    return not lines[y][right_limit].isnumeric() and lines[y][right_limit] != '.'


def is_left_bottom_diagonal(start, y):
    return y < height - 1 and not lines[y + 1][start - 1].isnumeric() and lines[y + 1][start - 1] != '.'


def is_left_top_diagonal(start, y):
    return y > 0 and not lines[y - 1][start - 1].isnumeric() and lines[y - 1][start - 1] != '.'


def is_left_neighbor(start, y):
    return not lines[y][start - 1].isnumeric() and lines[y][start - 1] != '.'


accumulator = ''
start = -1
size = 0

for y in range(height):
    if accumulator != '':
        if has_adjacent(start, size, y - 1):
            sum += int(accumulator)
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
            if has_adjacent(start, size, y):
                sum += int(accumulator)

            accumulator = ''
            start = -1
            size = 0

print(sum)
