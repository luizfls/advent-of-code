with open("input18.txt", "r") as f:
    lines = f.read().splitlines()

def evaluate(a, op, b):
    if op == '+':
        return a + b
    elif op == '*':
        return a * b

def compute_(s, total, op):
    if s[0].isdigit():
        space = s.find(' ')
        if space != -1:
            n = int(s[0:space])
            total = evaluate(total, op, n)
            return compute_(s[space + 3:], total, s[space + 1])
        else:
            n = int(s)
            total = evaluate(total, op, n)
            return total
    elif s[0] == '(':
        o = 0
        for i, c in enumerate(s[1:], 1):
            if c == '(':
                o += 1
            elif c == ')':
                if o > 0:
                    o -= 1
                else:
                    n = compute(s[1:i])
                    total = evaluate(total, op, n)
                    if i < len(s) - 1:
                        return compute_(s[i + 4:], total, s[i + 2])
                    else:
                        return total

def compute(s):
    return compute_(s, 0, '+')

total = 0
for line in lines:
    total += compute(line)

print total
