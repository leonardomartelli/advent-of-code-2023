import re

pattern = r'one|two|three|four|five|six|seven|eight|nine|\d'

numbers = {
    'one': 1,
    'two': 2,
    'three': 3,
    'four': 4,
    'five': 5,
    'six': 6,
    'seven': 7,
    'eight': 8,
    'nine': 9,
}


def parse(string):
    if string.isnumeric():
        return int(string)

    return numbers[string]


puzzle_input_file = open('input.txt', 'r')
puzzle_input = puzzle_input_file.read()

calibrations = puzzle_input.split('\n')

sum = 0

for calibration in calibrations:
    first, last = -1, -1

    caught = re.findall(pattern, calibration)

    if len(caught) == 1:
        first = last = parse(caught[0])
    else:
        first = parse(caught[0])
        last = parse(caught[len(caught) - 1])

    num = first*10 + last

    print(num)
    sum += num

print(sum)
