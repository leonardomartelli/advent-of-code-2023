puzzle_input_file = open('input.txt', 'r')
puzzle_input = puzzle_input_file.read()

cards = puzzle_input.split('\n')

sum = 0

for card in cards:
    numbers = card.split(':')[1]

    splitted_numbers = numbers.split('|')

    winning_numbers = set(splitted_numbers[0].split())
    my_numbers = set(splitted_numbers[1].split())

    matches = my_numbers.intersection(winning_numbers)

    if len(matches) > 0:
        sum += 2 ** (len(matches) - 1)

print(sum)
