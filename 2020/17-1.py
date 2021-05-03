import copy

with open("input17.txt", "r") as f:
    lines = map(list, f.read().splitlines())

d = len(lines)

c = dict((z, [['.' for j in xrange(d + 14)] for i in xrange(d + 14)]) for z in xrange(-7, 8))

for i, line in enumerate(lines):
    c[0][i + 7][7:7 + d] = line

def countNeighbors(c, i, j, z):
    total = 0
    for i_ in xrange(i - 1, i + 2):
        for j_ in xrange(j - 1, j + 2):
            for z_ in xrange(z - 1, z + 2):
                if i_ != i or j_ != j or z_ != z:
                    total += 1 if c[z_][i_][j_] == '#' else 0
    return total

def iterate(src):
    dst = copy.deepcopy(src)
    for z in xrange(-6, 7):
        for i, row in enumerate(src[z][1:-1], 1):
            for j, cell in enumerate(row[1:-1], 1):
                n = countNeighbors(src, i, j, z)
                if src[z][i][j] == '#' and not (n == 2 or n == 3):
                    dst[z][i][j] = '.'
                elif src[z][i][j] == '.' and n == 3:
                    dst[z][i][j] = '#'
    return dst

for i in xrange(6):
    c = iterate(c)

active = [cell for plane in c.itervalues() for row in plane for cell in row].count('#')
print active
