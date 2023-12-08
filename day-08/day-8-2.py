from itertools import cycle
from math import lcm

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
    if id[2] == 'A':
        actuals.append(id)

count = 0

loop_check = []

len_actuals = len(actuals)
result = 1

for actual in actuals:
    count = 0
    for instruction in cycle(instructions):

        actual = coordinates[actual][instruction]

        count += 1

        if actual[2] == 'Z':
            break

    result = lcm(result, count)

print(result)
