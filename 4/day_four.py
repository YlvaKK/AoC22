f = open('4/day_four_input')
lines = f.readlines()

overlapping_pairs = 0

def get_range(input):
    areas = input.split('-')

    return (int(areas[0]), int(areas[1]))

def contains_range(range1, range2):
    if (range1[0] <= range2[0] and range1[1] >= range2[1]) or (range2[0] <= range1[0] and range2[1] >= range1[1]):
        return True
    else:
        return False

def has_overlap(range1, range2):
    if contains_range(range1, range2):
        return True

    if (range1[0] >= range2[0] and range1[0] <= range2[1]) or (range2[0] >= range1[0] and range2[0] <= range1[1]):
        return True
    else:
        return False

for line in lines:
    print("line: %s" %line)
    pair = line.split(',')

    range1 = get_range(pair[0])
    range2 = get_range(pair[1])

    if has_overlap(range1, range2):
        overlapping_pairs += 1

print("pairs with any overlap: %s" %overlapping_pairs)

