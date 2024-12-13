def part_1():
    rows = []

    with open('day4input.txt', 'r') as file:
        for line in file:
            rows.append(line.strip())

    # for each x,y pos, count how many XMAS start here (out of 8)
    count = 0
    for y in range(len(rows)):
        for x in range(len(rows[y])):
            if rows[y][x] != 'X':
                continue
            # N
            if y >= 3:
                if rows[y-1][x] == 'M' and rows[y-2][x] == 'A' and rows[y-3][x] == 'S':
                    count += 1
            # E
            if x <= len(rows[y]) - 4:
                if rows[y][x+1] == 'M' and rows[y][x+2] == 'A' and rows[y][x+3] == 'S':
                    count += 1
            # S
            if y <= len(rows) - 4:
                if rows[y+1][x] == 'M' and rows[y+2][x] == 'A' and rows[y+3][x] == 'S':
                    count += 1
            # W
            if x >= 3:
                if rows[y][x-1] == 'M' and rows[y][x-2] == 'A' and rows[y][x-3] == 'S':
                    count += 1
            # NE
            if y >= 3 and x <= len(rows[y]) - 4:
                if rows[y-1][x+1] == 'M' and rows[y-2][x+2] == 'A' and rows[y-3][x+3] == 'S':
                    count += 1
            # SE
            if y <= len(rows) - 4 and x <= len(rows[y]) - 4:
                if rows[y+1][x+1] == 'M' and rows[y+2][x+2] == 'A' and rows[y+3][x+3] == 'S':
                    count += 1
            # SW
            if y <= len(rows) - 4 and x >= 3:
                if rows[y+1][x-1] == 'M' and rows[y+2][x-2] == 'A' and rows[y+3][x-3] == 'S':
                    count += 1
            # NW
            if y >= 3 and x >= 3:
                if rows[y-1][x-1] == 'M' and rows[y-2][x-2] == 'A' and rows[y-3][x-3] == 'S':
                    count += 1

    print(count)
    
def part_2():
    rows = []

    with open('day4input.txt', 'r') as file:
        for line in file:
            rows.append(line.strip())

    # analyzed pos is the A in Cross-MAS
    count = 0
    for y in range(len(rows)):
        for x in range(len(rows[y])):
            if rows[y][x] != 'A':
                continue
            has_ne = False
            has_nw = False
            if y >= 1 and y < len(rows) - 1 and x >= 1 and x < len(rows[y]) - 1:
                # ..S
                # .a.
                # M..
                if rows[y+1][x-1] == 'M' and rows[y-1][x+1] == 'S':
                    has_ne = True
                # ..M
                # .a.
                # S..
                elif rows[y-1][x+1] == 'M' and rows[y+1][x-1] == 'S':
                    has_ne = True
                # M..
                # .a.
                # ..S
                if rows[y-1][x-1] == 'M' and rows[y+1][x+1] == 'S':
                    has_nw = True
                # S..
                # .a.
                # ..M
                elif rows[y+1][x+1] == 'M' and rows[y-1][x-1] == 'S':
                    has_nw = True

                if(has_ne and has_nw):
                    count += 1

    print(count)

part_1()
part_2()