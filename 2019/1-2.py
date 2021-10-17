with open("input1.txt", "r") as f:
    masses = f.read().splitlines()
masses = list(map(int, masses))

def computeFuel(mass, mass2fuel):
    if mass <= 0:
        return 0
    elif mass not in mass2fuel:
        a = mass // 3 - 2
        mass2fuel[mass] = 0 if a < 0 else a + computeFuel(a, mass2fuel)
    return mass2fuel[mass]

mass2fuel = {}
total_fuel = 0
for mass in masses:
    total_fuel += computeFuel(mass, mass2fuel)

print(total_fuel)
