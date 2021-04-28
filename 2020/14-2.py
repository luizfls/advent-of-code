import copy

with open("input14.txt", "r") as f:
    lines = f.read().splitlines()

def applyMask(bits, mask):
    bits = bits.rjust(len(mask), '0')
    bits = list(bits)
    stop = -min(len(bits), len(mask)) - 1
    for i in xrange(-1, stop, -1):
        if mask[i] != '0':
            bits[i] = mask[i]
    return "".join(bits)

def expandAddress(address, addresses):
    if len(address) != 0:
        if address[0] != 'X':
            for a in addresses:
                a.append(address[0])
        else:
            addresses.extend(copy.deepcopy(addresses))
            for a in addresses[:len(addresses) // 2]:
                a.append('0')
            for a in addresses[len(addresses) // 2:]:
                a.append('1')
        expandAddress(address[1:], addresses)

mem = {}
for line in lines:
    if line[:4] == "mask":
        mask = line[7:]
    elif line[:3] == "mem":
        address = int(line[4 : line.find(']')])
        address = applyMask(bin(address)[2:], mask)
        addresses = [[]]
        expandAddress(address, addresses)
        addresses = map(lambda l: "".join(l), addresses)
        addresses = map(lambda s: int(s, 2), addresses)

        num = int(line[line.rfind('=') + 2:])

        for address in addresses:
            mem[address] = num

print sum(mem.itervalues())
