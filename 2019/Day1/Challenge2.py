with open("input.txt", "r") as file:
    content = file.readlines()

mass_ints = [int(i) for i in content]

fuelNeeded = 0

for mass in mass_ints:
    fuel = int(mass / 3)
    fuel = fuel-2
    fuelNeeded += fuel

    additionalFuel = fuel

    while additionalFuel >= 0:
        additionalFuel = int(additionalFuel/3-2)
        if additionalFuel >= 0:
            fuelNeeded += additionalFuel

print(fuelNeeded)
