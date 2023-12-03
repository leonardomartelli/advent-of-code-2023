puzzle_input_file = open('input.txt', 'r')
puzzle_input = puzzle_input_file.read()

games = puzzle_input.split('\n')


sum = 0

for game in games:
    splitted_id = game.split(':')

    id = int(splitted_id[0].split()[1])

    cubes_string = splitted_id[1]

    shows = cubes_string.split(';')
    invalid = False

    minimum_cubes = {
        'red': 0,
        'green': 0,
        'blue': 0,
    }

    for show in shows:
        cubes_set = show.split(',')

        for set in cubes_set:
            info = set.split()
            qnt = int(info[0])
            color = info[1]

            if minimum_cubes[color] < qnt:
                minimum_cubes[color] = qnt

    power = minimum_cubes['blue'] * \
        minimum_cubes['red'] * minimum_cubes['green']

    sum += power

print(sum)
