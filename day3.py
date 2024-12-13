import re

def part_1():
    input = ''

    with open('day3input.txt', 'r') as file:
        for line in file:
            input += line.strip()

    pattern = r"mul\(\d+,\d+\)"
    result = 0
    for match in re.findall(pattern, input):
        nums = re.findall(r"\d+", match)
        result += int(nums[0]) * int(nums[1])

    print(result)
    
def part_2():
    input = ''

    with open('day3input.txt', 'r') as file:
        for line in file:
            input += line.strip()

    pattern = r"mul\(\d+,\d+\)"
    result = 0
    enabled = True
    while True:
        mul = re.search(pattern, input)
        do_index = input.find('do()')
        dont_index = input.find('don\'t()')

        if(mul == None):
            break

        # do() next
        if(do_index != -1 and (dont_index == -1 or do_index < dont_index) and do_index < mul.start()):
            input = input[do_index + 4:]
            enabled = True
            continue

        # don't() next
        if(dont_index != -1 and (do_index == -1 or dont_index < do_index) and dont_index < mul.start()):
            input = input[dont_index + 7:]
            enabled = False
            continue
        
        #mul() next
        if(enabled):
            nums = re.findall(r"\d+", mul.group())
            result += int(nums[0]) * int(nums[1])

        input = input[mul.end():]

    print(result)

part_1()
part_2()