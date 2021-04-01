with open("input5.txt", "r") as f:
    lines = f.read().splitlines()

def decode(s, l, u):
    n = 0
    p = len(s) - 1
    for c in s:
        if c == u:
            n += 2 ** p
        p -= 1
    return n

def computeID(s):
    r = s[:7]
    c = s[7:]

    row = decode(r, 'F', 'B')
    col = decode(c, 'L', 'R')

    return row * 8 + col

max_id = -1
for line in lines:
    curr_id = computeID(line)
    max_id = max(max_id, curr_id)
print max_id
