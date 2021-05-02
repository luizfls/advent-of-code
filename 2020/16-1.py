with open("input16.txt", "r") as f:
    lines = f.read().splitlines()

ranges = []
for line in lines:
    if len(line) == 0:
        break
    intervals = line[line.find(':') + 2:]
    intervals = intervals.split(" or ")
    intervals = [interval.split('-') for interval in intervals]
    intervals = [tuple(map(int, interval)) for interval in intervals]
    ranges += intervals

def isValid(ranges, n):
    for lo, hi in ranges:
        if n >= lo and n <= hi:
            return True
    return False

tser = 0
i = lines.index("nearby tickets:")
for line in lines[i + 1:]:
    ticket = map(int, line.split(','))
    for num in ticket:
        if not isValid(ranges, num):
            tser += num

print tser
