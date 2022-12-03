f = open('3/day_three_input')
lines = f.readlines()

def get_value_of_item(char):
    if ord(char) >= ord('a'):
        return ord(char) - ord('a') + 1
    else:
        return ord(char) - ord('A') + 27

sum = 0

for line in lines:
    half_length = int(len(line) / 2)
    first_compartment = line[0 : half_length]
    second_compartment = line[half_length : len(line)]

    for char in first_compartment:
        if char in second_compartment:
            sum += get_value_of_item(char)
            print(char + " is in " + second_compartment)
            break

print("sum: %s" %sum)