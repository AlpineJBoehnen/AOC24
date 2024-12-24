from enum import Enum

class Direction(Enum):
    UP = 1
    RIGHT = 2
    DOWN = 3
    LEFT = 4

def part_1():        
    def get_map_symbol(map, x, y):
        if not in_map_bounds(map, x, y):
            return None
        return map[y][x]

    def set_map_symbol(map, x, y, symbol):
        map[y][x] = symbol

    def in_map_bounds(map, x, y):
        return 0 <= x < len(map[0]) and 0 <= y < len(map)

    def turn_right(map, guard_pos):
        set_map_symbol(map, guard_pos[0], guard_pos[1], guard_turns.get(get_map_symbol(map, guard_pos[0], guard_pos[1])))

    def is_blocked(map, guard_pos):
        guard = get_map_symbol(map, guard_pos[0], guard_pos[1])
        if guard == '^':
            return in_map_bounds(map, guard_pos[0], guard_pos[1] - 1) and get_map_symbol(map, guard_pos[0], guard_pos[1] - 1) == '#'
        if guard == '>':
            return in_map_bounds(map, guard_pos[0] + 1, guard_pos[1]) and get_map_symbol(map, guard_pos[0] + 1, guard_pos[1]) == '#'
        if guard == 'v':
            return in_map_bounds(map, guard_pos[0], guard_pos[1] + 1) and get_map_symbol(map, guard_pos[0], guard_pos[1] + 1) == '#'
        if guard == '<':
            return in_map_bounds(map, guard_pos[0] - 1, guard_pos[1]) and get_map_symbol(map, guard_pos[0] - 1, guard_pos[1]) == '#'

    def move_forward(map, guard_pos):
        guard = get_map_symbol(map, guard_pos[0], guard_pos[1])
        set_map_symbol(map, guard_pos[0], guard_pos[1], 'X')
        if guard == '^':    
            guard_pos = (guard_pos[0], guard_pos[1] - 1)
        elif guard == '>':
            guard_pos = (guard_pos[0] + 1, guard_pos[1])
        elif guard == 'v':
            guard_pos = (guard_pos[0], guard_pos[1] + 1)
        elif guard == '<':
            guard_pos = (guard_pos[0] - 1, guard_pos[1])
        if in_map_bounds(map, guard_pos[0], guard_pos[1]):
            set_map_symbol(map, guard_pos[0], guard_pos[1], guard)
        return guard_pos

    map = []
    guard_pos = (0,0) # x,y
    guard_turns = {'^': '>', '>': 'v', 'v': '<', '<': '^'}

    with open('day6input.txt', 'r') as file:
        lines = file.readlines()
        for y in range(len(lines)):
            for x in range(len(lines[y].strip())):
                if lines[y][x] in ['^', 'v', '<', '>']:
                    guard_pos = (x,y)
            map.append(list(lines[y].strip()))

    while True:
        if not in_map_bounds(map, guard_pos[0], guard_pos[1]):
            break
        if is_blocked(map, guard_pos):
            turn_right(map, guard_pos)
        else:
            guard_pos = move_forward(map, guard_pos)

    count_x = 0
    for y in range(len(map)):
        for x in range(len(map[y])):
            if map[y][x] == 'X':
                count_x += 1

    print(count_x)
    
def part_2():
    def get_map_symbol(map, x, y):
        if not in_map_bounds(map, x, y):
            return None
        return map[y][x]

    def in_map_bounds(map, x, y):
        return 0 <= x < len(map[0]) and 0 <= y < len(map)

    def turn_right(guard_dir):
        return guard_turns.get(guard_dir)

    def is_blocked(map, guard_pos, guard_dir):
        if guard_dir == Direction.UP:
            return in_map_bounds(map, guard_pos[0], guard_pos[1] - 1) and get_map_symbol(map, guard_pos[0], guard_pos[1] - 1) == '#'
        if guard_dir == Direction.RIGHT:
            return in_map_bounds(map, guard_pos[0] + 1, guard_pos[1]) and get_map_symbol(map, guard_pos[0] + 1, guard_pos[1]) == '#'
        if guard_dir == Direction.DOWN:
            return in_map_bounds(map, guard_pos[0], guard_pos[1] + 1) and get_map_symbol(map, guard_pos[0], guard_pos[1] + 1) == '#'
        if guard_dir == Direction.LEFT:
            return in_map_bounds(map, guard_pos[0] - 1, guard_pos[1]) and get_map_symbol(map, guard_pos[0] - 1, guard_pos[1]) == '#'

    def move_forward(guard_pos, guard_dir):
        if guard_dir == Direction.UP:    
            guard_pos = (guard_pos[0], guard_pos[1] - 1)
        elif guard_dir == Direction.RIGHT:
            guard_pos = (guard_pos[0] + 1, guard_pos[1])
        elif guard_dir == Direction.DOWN:
            guard_pos = (guard_pos[0], guard_pos[1] + 1)
        elif guard_dir == Direction.LEFT:
            guard_pos = (guard_pos[0] - 1, guard_pos[1])
        return guard_pos

    def is_next_move_origin(guard_pos, guard_dir, origin):
        if guard_dir == Direction.UP:
            return (guard_pos[0], guard_pos[1] - 1) == origin
        if guard_dir == Direction.RIGHT:
            return (guard_pos[0] + 1, guard_pos[1]) == origin
        if guard_dir == Direction.DOWN:
            return (guard_pos[0], guard_pos[1] + 1) == origin
        if guard_dir == Direction.LEFT:
            return (guard_pos[0] - 1, guard_pos[1]) == origin

    map = []
    guard_pos = (0,0) # x,y
    guard_dir = Direction.UP
    guard_turns = {
        Direction.UP: Direction.RIGHT, 
        Direction.RIGHT: Direction.DOWN, 
        Direction.DOWN: Direction.LEFT, 
        Direction.LEFT: Direction.UP}

    with open('day6input.txt', 'r') as file:
        lines = file.readlines()
        for y in range(len(lines)):
            for x in range(len(lines[y].strip())):
                cur = lines[y][x]
                if cur == '^':
                    guard_pos = (x,y)
                    guard_dir = Direction.UP
                elif cur == '>':
                    guard_pos = (x,y)
                    guard_dir = Direction.RIGHT
                elif cur == 'v':
                    guard_pos = (x,y)
                    guard_dir = Direction.DOWN
                elif cur == '<':
                    guard_pos = (x,y)
                    guard_dir = Direction.LEFT
            map.append(list(lines[y].strip()))

    start = (guard_pos[0], guard_pos[1], guard_dir)
    
    # less stupid (doesn't work)
    loops = 0
    # while True:
    #     if not in_map_bounds(map, guard_pos[0], guard_pos[1]):
    #         break
    #     if is_blocked(map, guard_pos, guard_dir):
    #         guard_dir = turn_right(guard_dir)
    #     else:
    #         if not is_next_move_origin(guard_pos, guard_dir, origin):
    #             sim_dir = turn_right(guard_dir) # simulate obstace placed in front of guard
    #             sim_pos = guard_pos
    #             sim_visited = set() # (x, y, dir)
    #             start = (sim_pos[0], sim_pos[1], guard_dir)
    #             while True:
    #                 cur = (sim_pos[0], sim_pos[1], sim_dir)
    #                 if cur in sim_visited or cur == start:
    #                     print("loop found at", guard_pos, guard_dir, len(sim_visited))
    #                     loops += 1
    #                     break
    #                 if not in_map_bounds(map, sim_pos[0], sim_pos[1]):
    #                     break
    #                 if is_blocked(map, sim_pos, sim_dir):
    #                     sim_dir = turn_right(sim_dir)
    #                 else:
    #                     sim_visited.add((sim_pos[0], sim_pos[1], sim_dir))
    #                     sim_pos = move_forward(sim_pos, sim_dir)
    #         guard_pos = move_forward(guard_pos, guard_dir)

    # stupid (works)
    total_dots = 0
    for y in range(len(map)):
        for x in range(len(map[y])):
            if get_map_symbol(map, x, y) == '.':
                total_dots += 1
    round = 0
    for y in range(len(map) - 1):
        for x in range(len(map[y]) - 1):
            if not get_map_symbol(map, x, y) == '.':
                continue
            round += 1
            print(round, "/", total_dots, "[", loops, "]")
            map[y][x] = '#'
            steps = 0
            while True:
                if(steps == 10000):
                    loops += 1
                    break
                if not in_map_bounds(map, guard_pos[0], guard_pos[1]):
                    break
                if is_blocked(map, guard_pos, guard_dir):
                    guard_dir = turn_right(guard_dir)
                else:
                    steps += 1
                    guard_pos = move_forward(guard_pos, guard_dir)
            map[y][x] = '.'
            guard_pos = (start[0], start[1])
            guard_dir = start[2]

    print(loops)

part_1()
part_2()