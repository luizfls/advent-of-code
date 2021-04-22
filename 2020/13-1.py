with open("input13.txt", "r") as f:
    lines = f.read().splitlines()

arrival = int(lines[0])
buses = sorted([int(bus) for bus in lines[1].split(',') if bus != 'x'])

waits = [(bus, bus - arrival % bus) for bus in buses]
waits = [(bus, 0) if bus == wait else (bus, wait) for bus, wait in waits]
waits = sorted(waits, key=lambda x: x[1])

print waits[0][0] * waits[0][1]
