with open("input12.txt", "r") as f:
    lines = f.read().splitlines()

lines = [(line[0], int(line[1:])) for line in lines]

direction = 0
x = y = 0

def rotate(sig, n):
    global direction
    direction += (sig * n)
    direction %= 360

for c, n in lines:
    if c == 'L' or c == 'R':
        rotate(1 if c == 'L' else -1, n)
    elif c == 'E' or c == 'F' and direction == 0:
        x += n
    elif c == 'N' or c == 'F' and direction == 90:
        y += n
    elif c == 'W' or c == 'F' and direction == 180:
        x -= n
    elif c == 'S' or c == 'F' and direction == 270:
        y -= n

print x, y
print abs(x) + abs(y)
