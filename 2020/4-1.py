with open("input4.txt", "r") as f:
    lines = f.read().splitlines()

required = frozenset(('byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'))
total = 0

fields = set()
for line in lines:
    if line:
        fields |= set([x.split(':')[0] for x in line.split()])
    else:
        fields.discard('cid')
        if fields == required:
            total += 1
        fields.clear()

print total
