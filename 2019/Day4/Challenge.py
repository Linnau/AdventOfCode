with open("input.txt", "r") as file:
    content = file.readline()

values = content.split('-')
first = int(values[0])
last = int(values[1])

numberOfPasswords = 0

for value in range(first, last):
    doubleFound = False
    decreases = False

    for idx, char in enumerate(str(value)):

        if idx == 0:
            continue

        digitBefore = int(str(value)[idx - 1])
        current = int(char)

        if current < digitBefore:
            decreases = True
            continue

        if current == digitBefore:
            doubleFound = True
            continue

    if doubleFound and not decreases:
        numberOfPasswords += 1

print(numberOfPasswords)  # Part 1

