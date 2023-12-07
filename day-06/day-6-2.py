puzzle_input_file = open('input.txt', 'r')
puzzle_input = puzzle_input_file.read()

inputs = puzzle_input.split('\n')
durations = [int(d) for d in inputs[0].replace(' ', '').split(':')[1:]]
records = [int(r) for r in inputs[1].replace(' ', '').split(':')[1:]]

possible_ways = 1

for i in range(len(durations)):
    race = durations[i]
    record = records[i]

    ways_to_beat = 0

    for possibilty in range(race):
        performance = (race - possibilty) * possibilty
        if performance > record:
            ways_to_beat += 1

    if ways_to_beat > 0:
        possible_ways *= ways_to_beat

print(possible_ways)
