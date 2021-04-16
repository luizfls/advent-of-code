import copy

with open("input11.txt", "r") as f:
    seatmap = f.read().splitlines()

seatmap = map(list, seatmap)

def countAdjacentOccupancy(seatmap, i, j):
    n = 0

    for xi in xrange(i - 1, -1, -1):
        if seatmap[xi][j] != '.':
            if seatmap[xi][j] == '#':
                n += 1
            break

    for xi in xrange(i + 1, len(seatmap)):
        if seatmap[xi][j] != '.':
            if seatmap[xi][j] == '#':
                n += 1
            break

    for xj in xrange(j - 1, -1, -1):
        if seatmap[i][xj] != '.':
            if seatmap[i][xj] == '#':
                n += 1
            break

    for xj in xrange(j + 1, len(seatmap[0])):
        if seatmap[i][xj] != '.':
            if seatmap[i][xj] == '#':
                n += 1
            break

    for xi, xj in zip(xrange(i - 1, -1, -1), xrange(j - 1, -1, -1)):
        if seatmap[xi][xj] != '.':
            if seatmap[xi][xj] == '#':
                n += 1
            break

    for xi, xj in zip(xrange(i + 1, len(seatmap)), xrange(j + 1, len(seatmap[0]))):
        if seatmap[xi][xj] != '.':
            if seatmap[xi][xj] == '#':
                n += 1
            break

    for xi, xj in zip(xrange(i + 1, len(seatmap)), xrange(j - 1, -1, -1)):
        if seatmap[xi][xj] != '.':
            if seatmap[xi][xj] == '#':
                n += 1
            break

    for xi, xj in zip(xrange(i - 1, -1, -1), xrange(j + 1, len(seatmap[0]))):
        if seatmap[xi][xj] != '.':
            if seatmap[xi][xj] == '#':
                n += 1
            break

    return n

def iterate(src, dst):
    for i, row in enumerate(src):
        for j, seat in enumerate(row):
            adj_occ = countAdjacentOccupancy(src, i, j)
            if seat == 'L' and adj_occ == 0:
                dst[i][j] = '#'
            elif seat == '#' and adj_occ >= 5:
                dst[i][j] = 'L'

changed = True
while changed:
    tmp = copy.deepcopy(seatmap)
    iterate(seatmap, tmp)
    changed = tmp != seatmap
    seatmap = tmp

occupied = [row.count('#') for row in seatmap]
print sum(occupied)
