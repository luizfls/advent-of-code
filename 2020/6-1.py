with open("input6.txt", "r") as f:
    lines = f.read().splitlines()

total = 0

answers = set()
for line in lines:
    if line:
        answers |= set(line)
    else:
        total += len(answers)
        answers.clear()

print total
