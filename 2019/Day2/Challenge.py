with open("input.txt", "r") as file:
    content = file.read()

inputValues = list(map(int, content.split(',')))
codes = inputValues.copy()

# Restore program


def calculator(noun, verb, intCodes):
    intCodes[1] = noun
    intCodes[2] = verb

    ix = 0
    while ix < len(intCodes):
        if intCodes[ix] == 1:  # Addition
            pos_a = intCodes[ix + 1]
            pos_b = intCodes[ix + 2]
            store_at = intCodes[ix + 3]
            intCodes[store_at] = intCodes[pos_a] + intCodes[pos_b]
            ix += 4
            continue

        if intCodes[ix] == 2:  # Multiplication
            pos_a = intCodes[ix + 1]
            pos_b = intCodes[ix + 2]
            store_at = intCodes[ix + 3]
            intCodes[store_at] = intCodes[pos_a] * intCodes[pos_b]
            ix += 4
            continue

        if intCodes[ix] == 99:  # HALT
            break

        # should switch here and print("ERROR!!") if not one of the correct values.

    return intCodes[0]


result = calculator(12, 2, codes)

print(result)

# Part Two
output = 19690720  # Value provided
codes = inputValues.copy()
for i in range(len(codes)):
    for j in range(len(codes)):
        codes = inputValues.copy()
        if calculator(i, j, codes) == output:
            print(100 * i + j)
            break

