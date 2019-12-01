with open("input.txt", "r") as file:
    content = file.readlines()

mass_ints = [int(i) for i in content]

fuelNeeded = 0

for mass in mass_ints:
    fuel = int(mass / 3)
    fuel = fuel-2
    fuelNeeded += fuel

print(fuelNeeded)