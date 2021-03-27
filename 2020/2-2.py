with open("input2.txt", "r") as f:
    lines = f.read().splitlines()

total = 0
for line in lines:
    s = line.split()
    (a, b) = map(int, s[0].split('-'))
    c = s[1][0]
    p = s[2]
    if (p[a - 1] == c) != (p[b - 1] == c):
        total += 1

print total
