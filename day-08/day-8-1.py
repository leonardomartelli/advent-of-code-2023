from itertools import cycle
puzzle_input_file = open('input.txt', 'r')
puzzle_input = puzzle_input_file.read()

splitted = puzzle_input.split('\n\n')

instructions = [0 if i == 'L' else 1 for i in splitted[0]]
raw_coordinates = splitted[1].split('\n')

coordinates = {}

first = None

actuals = []

for raw in raw_coordinates:
    splitted_coord = raw.split('=')
    id = splitted_coord[0].strip()
    neighbors = []
    splitted_neigh = splitted_coord[1].split()
    neighbors.append(splitted_neigh[0].strip()[1:-1])
    neighbors.append(splitted_neigh[1].strip()[:-1])
    coordinates[id] = neighbors

count = 0

loop_check = []
actual = 'AAA'

for instruction in cycle(instructions):

    actual = coordinates[actual][instruction]

    count += 1

    if actual == 'ZZZ':
        break


print(count)
