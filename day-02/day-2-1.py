puzzle_input_file = open('input.txt', 'r')
puzzle_input = puzzle_input_file.read()

games = puzzle_input.split('\n')

possible_cubes = {
    'red': 12,
    'green': 13,
    'blue': 14,
}

sum = 0

for game in games:
    splitted_id = game.split(':')

    id = int(splitted_id[0].split()[1])

    cubes_string = splitted_id[1]

    shows = cubes_string.split(';')
    invalid = False

    for show in shows:
        cubes_set = show.split(',')

        for set in cubes_set:
            info = set.split()
            qnt = int(info[0])
            color = info[1]

            if possible_cubes[color] < qnt:
                invalid = True
                break

    if not invalid:
        sum += id

print(sum)
