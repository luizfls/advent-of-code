with open("input16.txt", "r") as f:
    lines = f.read().splitlines()

# Parse rules
fields = set()
rules = {}
for line in lines:
    if len(line) == 0:
        break
    field = line[:line.find(':')]
    fields.add(field)
    intervals = line[line.find(':') + 2:]
    intervals = intervals.split(" or ")
    intervals = [interval.split('-') for interval in intervals]
    intervals = [tuple(map(int, interval)) for interval in intervals]
    rules[field] = intervals

intervals = [interval for intervals in rules.itervalues() for interval in intervals]

# Parse my ticket
i = lines.index("your ticket:")
my_ticket = map(int, lines[i + 1].split(','))

# Parse other tickets
def isValid(intervals, n):
    for lo, hi in intervals:
        if n >= lo and n <= hi:
            return True
    return False

tickets = []
i = lines.index("nearby tickets:")
for line in lines[i + 1:]:
    ticket = map(int, line.split(','))
    if all([isValid(intervals, num) for num in ticket]):
        tickets.append(ticket)

# Infer columns
column2fields = dict((i, set(fields)) for i in xrange(len(tickets[0])))

for i in xrange(len(tickets[0])):
    for t in tickets:
        for field, intervals in rules.iteritems():
            if not isValid(intervals, t[i]):
                column2fields[i].discard(field)
        if len(column2fields[i]) <= 1:
            break

column2fields = sorted(column2fields.items(), key=lambda x: len(x[1]))
for i, (column, fields) in enumerate(column2fields):
    for c, fs in column2fields[i + 1:]:
        for f in fields:
            fs.discard(f)

# "departure" columns
dc = sorted([column for column, fields in column2fields if "departure" in next(iter(fields))])

# Compute product
d = 1
for col in dc:
    print my_ticket[col],
    d *= my_ticket[col]

print "\n", d
