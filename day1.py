def part_1():
    array_1 = []
    array_2 = []

    with open('day1input.txt', 'r') as file:
        for line in file:
            parts = line.split('   ')
            array_1.append(int(parts[0].strip()))
            array_2.append(int(parts[1]))

    array_1.sort()
    array_2.sort()

    dist = 0
    for i in range(len(array_1)):
        dist += abs(int(array_1[i]) - int(array_2[i]))

    print(dist)

def part_2():
    array_1 = []
    array_2 = []

    with open('day1input.txt', 'r') as file:
        for line in file:
            parts = line.split('   ')
            array_1.append(int(parts[0]))
            array_2.append(int(parts[1]))

    similarity = 0
    for i in range(len(array_1)):
        num = int(array_1[i])
        similarity += num * array_2.count(num)

    print(similarity)

part_1()
part_2()