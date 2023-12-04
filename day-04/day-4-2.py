puzzle_input_file = open('input.txt', 'r')
puzzle_input = puzzle_input_file.read()

cards = puzzle_input.split('\n')

scratchcards = [1 for _ in cards]


for i, card in enumerate(cards):
    numbers = card.split(':')[1]

    splitted_numbers = numbers.split('|')

    winning_numbers = set(splitted_numbers[0].split())
    my_numbers = set(splitted_numbers[1].split())

    matches = my_numbers.intersection(winning_numbers)

    for repetition in range(scratchcards[i]):
        for s in range(i+1, i+1+len(matches)):
            scratchcards[s] += 1

print(sum(scratchcards))
