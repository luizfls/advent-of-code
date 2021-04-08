with open("input8.txt", "r") as f:
    lines = f.read().splitlines()

lines = [(line[0:3], line[4:5], int(line[5:])) for line in lines]
lines = [(line[0], line[2] * (-1) if line[1] == '-' else line[2]) for line in lines]

i = 0
visited = set()
acc = 0
while i not in visited:
    visited.add(i)

    (op, n) = lines[i]
    if op == 'acc':
        acc += n
        i += 1
    elif op == 'jmp':
        i += n
    elif op == 'nop':
        i += 1

print acc
