with open("input8.txt", "r") as f:
    lines = f.read().splitlines()

lines = [(line[0:3], line[4:5], int(line[5:])) for line in lines]
lines = [(line[0], line[2] * (-1) if line[1] == '-' else line[2]) for line in lines]

def execute(lines):
    i = 0
    visited = set()
    acc = 0
    while i not in visited and i >= 0 and i < len(lines):
        visited.add(i)

        (op, n) = lines[i]
        if op == 'acc':
            acc += n
            i += 1
        elif op == 'jmp':
            i += n
        elif op == 'nop':
            i += 1

    return (i == len(lines), acc)

for i, line in enumerate(lines):
    (op, n) = line
    if op == 'jmp':
        lines[i] = ('nop', n)
    elif op == 'nop':
        lines[i] = ('jmp', n)
    elif op == 'acc':
        continue

    (ans, acc) = execute(lines)

    if ans:
        print acc
        break
    else:
        lines[i] = line
