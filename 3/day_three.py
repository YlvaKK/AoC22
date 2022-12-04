f = open('3/day_three_input')
lines = f.readlines()

def get_value_of_item(char):
    if ord(char) >= ord('a'):
        return ord(char) - ord('a') + 1
    else:
        return ord(char) - ord('A') + 27

def part_one(lines):
    sum = 0

    for line in lines:
        half_length = int(len(line) / 2)
        first_compartment = line[0 : half_length]
        second_compartment = line[half_length : len(line)]

        for char in first_compartment:
            if char in second_compartment:
                sum += get_value_of_item(char)
                break

    print("     sum: %s" %sum)

def part_two(lines):
    sum = 0

    for i in range(0, len(lines), 3):
        first_line = lines[i]
        second_line = lines[i+1]
        third_line = lines[i+2]

        for char in first_line:
            if char in second_line and char in third_line:
                sum += get_value_of_item(char)
                break
    
    print("     sum: %s" %sum)

print("part one: ")
part_one(lines)
print("part_two: ")
part_two(lines)
