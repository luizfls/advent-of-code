from operator import mul
from collections import deque

with open("input10.txt", "r") as f:
    lines = f.read().splitlines()

nums = sorted(map(int, lines))
nums.insert(0, 0)
nums.append(nums[-1] + 3)

prev = -1
groups = []
subgroup = []
for num in nums:
    if num - prev == 3:
        groups.append(subgroup)
        subgroup = []

    subgroup.append(num)
    prev = num

groups.append(subgroup)

groups = [group for group in groups if len(group) >= 3]

def buildGraph(group):
    graph = {}
    for i, num in enumerate(group):
        graph[num] = []
        for j in xrange(i + 1, len(group)):
            if group[j] - num <= 3:
                graph[num].append(group[j])
            else:
                break
    return graph

def countPaths(graph):
    total = 0
    s = deque()
    s.append(min(graph.iterkeys()))
    while len(s) > 0:
        nexts = graph[s.pop()]
        if len(nexts) == 0:
            total += 1
        else:
            for next in reversed(nexts):
                s.append(next)
    return total

combinations = [countPaths(buildGraph(group)) for group in groups]
print reduce(mul, combinations, 1)
