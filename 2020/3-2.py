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

a = countTrees(lines, 1, 1)
b = countTrees(lines, 3, 1)
c = countTrees(lines, 5, 1)
d = countTrees(lines, 7, 1)
e = countTrees(lines, 1, 2)

print a, b, c, d, e
print a * b * c * d * e
