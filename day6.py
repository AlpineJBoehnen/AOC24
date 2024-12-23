def part_1():
    map = []
    guard_pos = (-1,-1)

    with open('day6input.txt', 'r') as file:
        for line in file:
            map.append(list(line.strip()))

    # get guard start position
    for y in range(len(map)):
        for x in range(len(map[y])):
            if map[y][x] in ['^', 'v', '<', '>']:
                guard_pos = (x,y)

    map_height = len(map)
    map_width = len(map[0])

    # Move guard while in bounds
    while in_bounds(guard_pos[0], guard_pos[1], map_width, map_height):
        guard = map[guard_pos[1]][guard_pos[0]]

        # If guard is facing down
        if guard == 'v':
            # Check bounds before accessing the map
            if guard_pos[1] + 1 < map_height and map[guard_pos[1] + 1][guard_pos[0]] == '#':
                # Turn right
                map[guard_pos[1]][guard_pos[0]] = '<'
            else:
                # Move down if within bounds
                if guard_pos[1] + 1 < map_height:
                    map[guard_pos[1] + 1][guard_pos[0]] = 'v'
                map[guard_pos[1]][guard_pos[0]] = 'X'
                guard_pos = (guard_pos[0], guard_pos[1] + 1)

        # If guard is facing left
        elif guard == '<':
            # Check bounds before accessing the map
            if guard_pos[0] - 1 >= 0 and map[guard_pos[1]][guard_pos[0] - 1] == '#':
                # Turn right
                map[guard_pos[1]][guard_pos[0]] = '^'
            else:
                # Move left if within bounds
                if guard_pos[0] - 1 >= 0:
                    map[guard_pos[1]][guard_pos[0] - 1] = '<'
                map[guard_pos[1]][guard_pos[0]] = 'X'
                guard_pos = (guard_pos[0] - 1, guard_pos[1])

        # If guard is facing right
        elif guard == '>':
            # Check bounds before accessing the map
            if guard_pos[0] + 1 < map_width and map[guard_pos[1]][guard_pos[0] + 1] == '#':
                # Turn right
                map[guard_pos[1]][guard_pos[0]] = 'v'
            else:
                # Move right if within bounds
                if guard_pos[0] + 1 < map_width:
                    map[guard_pos[1]][guard_pos[0] + 1] = '>'
                map[guard_pos[1]][guard_pos[0]] = 'X'
                guard_pos = (guard_pos[0] + 1, guard_pos[1])

        # If guard is facing up
        elif guard == '^':
            # Check bounds before accessing the map
            if guard_pos[1] - 1 >= 0 and map[guard_pos[1] - 1][guard_pos[0]] == '#':
                # Turn right
                map[guard_pos[1]][guard_pos[0]] = '>'
            else:
                # Move up if within bounds
                if guard_pos[1] - 1 >= 0:
                    map[guard_pos[1] - 1][guard_pos[0]] = '^'
                map[guard_pos[1]][guard_pos[0]] = 'X'
                guard_pos = (guard_pos[0], guard_pos[1] - 1)

    count_x = 0
    for y in range(len(map)):
        for x in range(len(map[y])):
            if map[y][x] == 'X':
                count_x += 1

    print(count_x)
    
def part_2():
    array_1 = []

    with open('day6input.txt', 'r') as file:
        for line in file:
            array_1.append(line.strip())

    for line in array_1:
        print(line)

def in_bounds(x, y, width, height):
    return x >= 0 and x < width and y >= 0 and y < height

part_1()
part_2()