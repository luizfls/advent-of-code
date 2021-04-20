with open("input12.txt", "r") as f:
    lines = f.read().splitlines()

lines = [(line[0], int(line[1:])) for line in lines]
lines = [('R', 90) if c == 'L' and n == 270 else (c, n) for c, n in lines]
lines = [('L', 90) if c == 'R' and n == 270 else (c, n) for c, n in lines]

dwx = 10
dwy = 1
x = y = 0

def rotate(direction, n):
    global dwx
    global dwy
    if n == 180:
        dwx *= -1
        dwy *= -1
    elif direction == 'L':
        dwx, dwy = -dwy, dwx
    elif direction == 'R':
        dwx, dwy = dwy, -dwx

for c, n in lines:
    if c == 'E':
        dwx += n
    elif c == 'N':
        dwy += n
    elif c == 'W':
        dwx -= n
    elif c == 'S':
        dwy -= n
    elif c == 'L' or c == 'R':
        rotate(c, n)
    else:
        x += n * dwx
        y += n * dwy

print x, y
print abs(x) + abs(y)
