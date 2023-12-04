puzzle_input_file = open('input.txt', 'r')
puzzle_input = puzzle_input_file.read()

calibrations = puzzle_input.split('\n')

sum = 0

for calibration in calibrations:
    first, last = -1, -1

    for char in calibration:
        if not char.isnumeric():
            continue

        if first == -1:
            first = last = int(char)
        else:
            last = int(char)

    num = first*10 + last

    sum += num

print(sum)
