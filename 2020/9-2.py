with open("input9.txt", "r") as f:
    lines = f.read().splitlines()

nums = map(int, lines)

goal = 25918798

def findSum(nums, i, goal):
    partial = 0
    for j in xrange(i, len(nums)):
        partial += nums[j]
        if partial == goal:
            return (True, min(nums[i:j + 1]) + max(nums[i:j + 1]))
        elif partial > goal:
            return (False, None)

for i in range(len(nums)):
    (ans, n) = findSum(nums, i, goal)
    if ans:
        print n
        break
