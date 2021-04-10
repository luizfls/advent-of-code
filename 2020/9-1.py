with open("input9.txt", "r") as f:
    lines = f.read().splitlines()

nums = map(int, lines)

w = 25
counter = {}
for num in nums[:w]:
    if num in counter:
        counter[num] += 1
    else:
        counter[num] = 1

def searchTwoElementsSum(counter, num):
    for (n, count) in counter.iteritems():
        if (num - n == n and count > 1) or (num - n != n and num - n in counter):
            return True
    return False

i = 0
for num in nums[w:]:
    if not searchTwoElementsSum(counter, num):
        print num
        break

    old = nums[i]
    new = num

    if old != new:
        counter[old] -= 1
        if counter[old] == 0:
            del counter[old]

        if new in counter:
            counter[new] += 1
        else:
            counter[new] = 1

    i += 1
