def part_1():
    reports = []

    with open('day2input.txt', 'r') as file:
        for line in file:
            reports.append([int(x) for x in line.split(' ')])

    safe = 0
    for report in reports:
        safe += report_is_safe(report)

    print(safe)

def part_2():
    reports = []

    with open('day2input.txt', 'r') as file:
        for line in file:
            reports.append([int(x) for x in line.split(' ')])

    safe = 0
    for report in reports:
        if(report_is_safe(report)):
            safe += 1
            continue

        # try removing one element
        is_safe = False
        for i in range(len(report)):
            if(report_is_safe(report[:i] + report[i+1:])):
                is_safe = True
                break
        if is_safe:
            safe += 1
            continue

    print(safe)

def report_is_safe(levels):
    unsafe = False
    hasIncreased = False
    hasDecreased = False
    for i in range(len(levels) - 1):
        if levels[i] > levels[i + 1]:
            hasDecreased = True
        elif levels[i] < levels[i + 1]:
            hasIncreased = True
        if hasIncreased and hasDecreased:
            unsafe = True
            break
        diff = abs(levels[i] - levels[i + 1])
        if diff < 1 or diff > 3:
            unsafe = True
            break
    return unsafe == False

part_1()
part_2()