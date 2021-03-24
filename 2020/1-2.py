import bisect

def searchThreeElementsSum(v, s):
    for i, n1 in enumerate(v):
        if(n1 > 2020 // 3):
            return None
        for j in xrange(i + 1, len(v)):
            if(v[j] > (2020 - n1) // 2):
                break
            c = 2020 - n1 - v[j]
            k = bisect.bisect(v, c, j + 1) - 1
            if k < len(v) and v[k] == c:
                return (i, j, k)

v = []
with open("input1.txt", "r") as f:
    v = f.read().splitlines()
v = map(int, v)

v = sorted(v)

x = searchThreeElementsSum(v, 2020)

if x is not None:
    (i, j, k) = x
    print v[i], v[j], v[k]
    print v[i] * v[j] * v[k]
else:
    print "N/A"
