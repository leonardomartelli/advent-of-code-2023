import re

numbers = {
    'one': 'o1e',
    'two': 't2o',
    'three': 't3e',
    'four': 'f4r',
    'five': 'f5e',
    'six': 's6x',
    'seven': 's7n',
    'eight': 'e8t',
    'nine': 'n9e',
}

puzzle_input_file = open('input.txt', 'r')
puzzle_input = puzzle_input_file.read()

calibrations = puzzle_input.split('\n')

sum = 0

for calibration in calibrations:
    first, last = -1, -1

    for key in numbers:
        calibration = calibration.replace(key, numbers[key])

    caught = re.findall('\d', calibration)

    if len(caught) == 1:
        first = last = int(caught[0])
    else:
        first = int(caught[0])
        last = int(caught[len(caught) - 1])

    num = first*10 + last

    print(calibration, caught, num)
    sum += num

print(sum)
