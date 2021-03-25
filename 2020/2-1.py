with open("input2.txt", "r") as f:
    lines = f.read().splitlines()

total = 0
for line in lines:
    s = line.split()
    (lo, hi) = map(int, s[0].split('-'))
    c = s[1][0]
    p = s[2]
    n = p.count(c)
    if n >= lo and n <= hi:
        total += 1

print total
