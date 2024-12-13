def part_1():
    array_1 = []

    with open('day1input.txt', 'r') as file:
        for line in file:
            array_1.append(line.strip())

    print('read ' + str(len(array_1)) + ' lines')
    
def part_2():
    array_1 = []

    with open('day1input.txt', 'r') as file:
        for line in file:
            array_1.append(line.strip())

    print('read ' + str(len(array_1)) + ' lines')

part_1()
part_2()