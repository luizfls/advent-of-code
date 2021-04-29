input_ = [9, 6, 0, 10, 18, 2, 1]

history = {}

for i, n in enumerate(input_, 1):
    history[n] = [i]

turn = len(history) + 1
curr = input_[-1]
while turn <= 2020:
    if len(history[curr]) == 1:
        curr = 0
    else:
        curr = history[curr][-1] - history[curr][-2]

    if curr not in history:
        history[curr] = [turn]
    else:
        history[curr].append(turn)
    turn += 1

print curr
