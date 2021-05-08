from collections import deque

with open("input22.txt", "r") as f:
    lines = f.read().splitlines()

d1 = deque(map(int, lines[1:lines.index("")]))
d2 = deque(map(int, lines[lines.index("") + 2:]))

while len(d1) > 0 and len(d2) > 0:
    c1 = d1.popleft()
    c2 = d2.popleft()

    if c1 > c2:
        d1.extend([c1, c2])
    else:
        d2.extend([c2, c1])

winner = d1 if len(d1) > 0 else d2

total = 0
for i, n in enumerate(reversed(winner), 1):
    total += n * i

print total
