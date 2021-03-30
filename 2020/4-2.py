with open("input4.txt", "r") as f:
    lines = f.read().splitlines()

def validateColor(color):
    return len(color) == 7 and color[0] == '#' and all(c.isdigit() or (c >= 'a' and c <= 'f') for c in color[1:])

def validate(passport):
    required = frozenset(('byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'))
    ecls = frozenset(('amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'))

    if set(passport) != required:
        return False

    byr = int(passport['byr'])
    if byr < 1920 or byr > 2002:
        return False

    iyr = int(passport['iyr'])
    if iyr < 2010 or iyr > 2020:
        return False

    eyr = int(passport['eyr'])
    if eyr < 2020 or eyr > 2030:
        return False

    if len(passport['hgt']) < 4:
        return False
    else:
        hgt = int(passport['hgt'][:-2])
        if passport['hgt'][-2:] == 'cm' and (hgt < 150 or hgt > 193):
            return False
        elif passport['hgt'][-2:] == 'in' and (hgt < 59 or hgt > 76):
            return False

    if not validateColor(passport['hcl']):
        return False

    if passport['ecl'] not in ecls:
        return False

    if len(passport['pid']) != 9 or not passport['pid'].isdigit():
        return False

    return True

total = 0
passport = {}
for line in lines:
    if line:
        line = [x.split(':') for x in line.split()]
        for key, value in line:
            passport[key] = value
    else:
        try:
            if 'cid' in passport:
                del passport['cid']
            if validate(passport):
                total += 1
        except:
            pass

        passport.clear()

print total
