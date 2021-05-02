from collections import deque
from collections import defaultdict

with open("input7.txt", "r") as f:
    lines = f.read().splitlines()

def line2colors(s):
    n = s.count(',')
    s = s.split()
    colors = [s[0] + ' ' + s[1]]
    for i in xrange(4, 4 * n + 5, 4):
        colors.append((int(s[i]), s[i + 1] + ' ' + s[i + 2]))
    return colors

g = defaultdict(list)
for line in lines:
    if line[-14:-1] == 'no other bags':
        continue
    colors = line2colors(line)
    for w, color in colors[1:]:
        g[colors[0]].append((w, color))

def count(g, color):
    total = 0
    for w, neighbor in g[color]:
        total += w + w * count(g, neighbor)
    return total

print count(g, 'shiny gold')
