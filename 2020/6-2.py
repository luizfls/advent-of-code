with open("input6.txt", "r") as f:
    lines = f.read().splitlines()

total = 0

answers = set()
new_group = True
for line in lines:
    if line:
        if new_group:
            answers |= set(line)
        else:
            answers &= set(line)
        new_group = False
    else:
        total += len(answers)
        answers.clear()
        new_group = True

print total
