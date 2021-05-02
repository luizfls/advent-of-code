from collections import deque
from collections import defaultdict

with open("input7.txt", "r") as f:
    lines = f.read().splitlines()

def line2colors(s):
    n = s.count(',')
    s = s.split()
    colors = [s[0] + ' ' + s[1]]
    for i in xrange(5, 4 * n + 6, 4):
        colors.append(s[i] + ' ' + s[i + 1])
    return colors

g = defaultdict(list)
for line in lines:
    if line[-14:-1] == 'no other bags':
        continue
    colors = line2colors(line)
    for color in colors[1:]:
        g[color].append(colors[0])

def count(g, color):
    visited = set()
    d = deque([color])
    while len(d) > 0:
        color = d.pop()
        if color not in visited:
            visited.add(color)
            for c in g[color]:
                d.append(c)
    return len(visited) - 1

print count(g, 'shiny gold')
