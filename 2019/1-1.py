with open("input1.txt", "r") as f:
    masses = f.read().splitlines()
masses = list(map(int, masses))

total_fuel = 0
for mass in masses:
    total_fuel += (mass // 3 - 2)

print(total_fuel)
