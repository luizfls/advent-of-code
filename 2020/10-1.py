with open("input10.txt", "r") as f:
    lines = f.read().splitlines()

nums = map(int, lines)
nums = sorted(nums)

prev = 0
dif1 = 0
dif3 = 1
for num in nums:
    if num - prev == 1:
        dif1 += 1
    if num - prev == 3:
        dif3 += 1

    prev = num

print dif1 * dif3
