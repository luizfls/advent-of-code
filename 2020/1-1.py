import bisect

def searchTwoElementsSum(v, s):
    for i, num in enumerate(v):
        if(num > 1010):
            return None
        c = 2020 - num
        j = bisect.bisect(v, c, i + 1) - 1
        if j < len(v) and v[j] == c:
            return (i, j)

v = []
with open("input1.txt", "r") as f:
    v = f.read().splitlines()
v = map(int, v)

v = sorted(v)

x = searchTwoElementsSum(v, 2020)

if x is not None:
    (i, j) = x
    print v[i], v[j]
    print v[i] * v[j]
else:
    print "N/A"
