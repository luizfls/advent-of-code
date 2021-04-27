with open("input14.txt", "r") as f:
    lines = f.read().splitlines()

def applyMask(bits, mask):
    bits = bits.rjust(len(mask), '0')
    bits = list(bits)
    stop = -min(len(bits), len(mask)) - 1
    for i in xrange(-1, stop, -1):
        if mask[i] != 'X':
            bits[i] = mask[i] 
    return int("".join(bits), 2)

mem = {}
for line in lines:
    if line[:4] == "mask":
        mask = line[7:]
    elif line[:3] == "mem":
        addr = int(line[4:line.find(']')])
        num = int(line[line.rfind('=') + 2:])
        mem[addr] = applyMask(bin(num)[2:], mask)

print sum(mem.itervalues())
