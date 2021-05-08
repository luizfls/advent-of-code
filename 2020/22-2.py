from collections import deque
import itertools

with open("input22.txt", "r") as f:
    lines = f.read().splitlines()

d1 = deque(map(int, lines[1:lines.index("")]))
d2 = deque(map(int, lines[lines.index("") + 2:]))

def playGame(d1, d2):
    previous_hands1 = []
    previous_hands2 = []

    while len(d1) > 0 and len(d2) > 0:
        if d1 in previous_hands1 or d2 in previous_hands2:
            return True

        previous_hands1.append(deque(d1))
        previous_hands2.append(deque(d2))

        c1 = d1.popleft()
        c2 = d2.popleft()

        if c1 <= len(d1) and c2 <= len(d2):
            winnerIsP1 = playGame(deque(itertools.islice(d1, 0, c1)), deque(itertools.islice(d2, 0, c2)))
        else:
            winnerIsP1 = c1 > c2

        if winnerIsP1:
            d1.extend([c1, c2])
        else:
            d2.extend([c2, c1])

    return len(d1) > 0

winnerIsP1 = playGame(d1, d2)
winner = d1 if winnerIsP1 else d2

total = 0
for i, n in enumerate(reversed(winner), 1):
    total += n * i

print total
