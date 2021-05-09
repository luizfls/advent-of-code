input_ = [2, 5, 3, 1, 4, 9, 8, 6, 7]

class Node:
    def __init__(self, value = None):
        self.value = value
        self.next = None

# cll: circular linked list
cll = None
for i in reversed(input_):
    n = Node(i)
    n.next = cll
    cll = n

p = cll
while p.next is not None:
    p = p.next
p.next = cll

def find(cll, destination):
    p = cll
    while p is not None:
        if p.value == destination:
            return p
        p = p.next
    return None

# c: current
# d: destination
c = cll
for _ in xrange(100):
    p = c.next
    c.next = c.next.next.next.next
    forbidden = set([c.value, p.value, p.next.value, p.next.next.value])
    destination = c.value
    while destination in forbidden:
        destination = (destination - 2) % 9 + 1
    d = find(cll, destination)
    p.next.next.next = d.next
    d.next = p
    c = c.next

p = find(cll, 1).next
result = ""
while p.value != 1:
    result += str(p.value)
    p = p.next

print result
