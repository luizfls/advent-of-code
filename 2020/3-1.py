def countTrees(M, r, d):
    j = 0
    trees = 0
    for i in xrange(0, len(M), d):
        if i != 0 and M[i][j] == '#':
            trees += 1
        j = (j + r) % len(M[0])
    return trees

lines = []
with open("input3.txt", "r") as f:
    lines = f.read().splitlines()

print countTrees(lines, 3, 1)
