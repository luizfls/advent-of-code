import copy

with open("input11.txt", "r") as f:
    seatmap = f.read().splitlines()

seatmap = map(list, seatmap)

def countAdjacentOccupancy(seatmap, i, j):
    n = 0
    for xi in xrange(i - 1, i + 2):
        for xj in xrange(j - 1, j + 2):
            if xi != i or xj != j:
                if xi >= 0 and xi < len(seatmap) and xj >= 0 and xj < len(seatmap[0]) and seatmap[xi][xj] == '#':
                    n += 1
    return n

def iterate(src, dst):
    for i, row in enumerate(src):
        for j, seat in enumerate(row):
            adj_occ = countAdjacentOccupancy(src, i, j)
            if seat == 'L' and adj_occ == 0:
                dst[i][j] = '#'
            elif seat == '#' and adj_occ >= 4:
                dst[i][j] = 'L'

changed = True
while changed:
    tmp = copy.deepcopy(seatmap)
    iterate(seatmap, tmp)
    changed = tmp != seatmap
    seatmap = tmp

occupied = [row.count('#') for row in seatmap]
print sum(occupied)
