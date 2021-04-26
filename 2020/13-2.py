with open("input13.txt", "r") as f:
    line = f.read().splitlines()[-1]

line = line.split(',')
d_ref = int(line[0])
line = enumerate(line[1:], 1)
line = [(b, a) for a, b in line]
buses = [bus for bus in line if bus[0] != 'x']
buses = [(int(bus[0]), bus[1]) for bus in buses]
buses = sorted(buses, reverse=True)

t = 0
(d, offset) = buses[0]
while True:
    if (t + offset) % d == 0:
        break
    t += d_ref

def checkBuses(t, buses):
    for (d, offset) in buses:
        if (t + offset) % d != 0:
            return False
    return True

while True:
    if checkBuses(t, buses[1:]):
        break
    t += d_ref * buses[0][1]

print t
