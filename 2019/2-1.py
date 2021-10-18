with open("input2.txt", "r") as f:
    ints = f.read().splitlines()[0]
ints = list(map(int, ints.split(',')))
ints[1] = 12
ints[2] = 2

c = 0
while ints[c] != 99:
    if ints[c] == 1:
        ints[ints[c + 3]] = ints[ints[c + 1]] + ints[ints[c + 2]]
    elif ints[c] == 2:
        ints[ints[c + 3]] = ints[ints[c + 1]] * ints[ints[c + 2]]
    c += 4

print(ints[0])
