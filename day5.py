class Rule:
    def __init__(self, left, right):
        self.left = left
        self.right = right

def part_1():
    rules = []
    updates = []

    with open('day5input.txt', 'r') as file:
        seenBlank = False
        for line in file:
            if line == '\n':
                seenBlank = True
                continue
            elif seenBlank:
                updates.append([int(x) for x in line.strip().split(',')])
            else:
                parts = line.strip().split('|')
                rules.append(Rule(int(parts[0]), int(parts[1])))

    good_updates = []
    for update in updates:
        bad = False
        for ii in range(len(update)):
            val = update[ii]
            left_vals = update[:ii]
            right_vals = update[ii + 1:]
            must_be_right = [rule.right for rule in rules if rule.left == val]
            must_be_left = [rule.left for rule in rules if rule.right == val]
            for left_val in left_vals:
                if left_val in must_be_right:
                    bad = True
                    break
            for right_val in right_vals:
                if(bad):
                    break
                if right_val in must_be_left:
                    bad = True
                    break
            if(bad):
                break
        if(bad):
            continue
        good_updates.append(update)

    sum = 0
    for update in good_updates:
        # add value of middle element (update is always odd length) to sum
        sum += update[len(update) // 2]

    print(str(sum))
    
def part_2():
    rules = []
    updates = []

    with open('day5input.txt', 'r') as file:
        seenBlank = False
        for line in file:
            if line == '\n':
                seenBlank = True
                continue
            elif seenBlank:
                updates.append([int(x) for x in line.strip().split(',')])
            else:
                parts = line.strip().split('|')
                rules.append(Rule(int(parts[0]), int(parts[1])))

    bad_updates = []
    for update in updates:
        bad = False
        for ii in range(len(update)):
            val = update[ii]
            left_vals = update[:ii]
            right_vals = update[ii + 1:]
            must_be_right = [rule.right for rule in rules if rule.left == val]
            must_be_left = [rule.left for rule in rules if rule.right == val]
            for left_val in left_vals:
                if left_val in must_be_right:
                    bad = True
                    break
            for right_val in right_vals:
                if(bad):
                    break
                if right_val in must_be_left:
                    bad = True
                    break
            if(bad):
                break
        if(bad):
            bad_updates.append(update)

    for update in bad_updates:
        while True:
            swapped = False
            for ii in range(len(update) - 1):
                if update[ii] in [rule.right for rule in rules if rule.left == update[ii + 1]]:
                    update[ii], update[ii + 1] = update[ii + 1], update[ii]
                    swapped = True
            if not swapped:
                break

    sum = 0
    for update in bad_updates:
        # add value of middle element (update is always odd length) to sum
        sum += update[len(update) // 2]

    print(str(sum))

part_1()
part_2()