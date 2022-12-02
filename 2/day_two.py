def match_result(opponent, you):
    if draw[opponent] == you:
        return 3
    elif wins_over[opponent] == you:
        return 6
    else:
        return 0

draw = { "A": "X", "B": "Y", "C": "Z" }
wins_over = { "C": "X", "A": "Y", "B": "Z" }
loses_to = { "B": "X", "C": "Y", "A": "Z" }

shape_points = { "X": 1, "Y": 2, "Z": 3 }
points = 0

with open('2/day_two_input') as f:
        lines = f.readlines()

for line in lines:
    shapes = line.split(" ")
    opponent, outcome = shapes[0].strip(), shapes[1].strip()

    if outcome == "X":
        you = loses_to[opponent]
    elif outcome == "Y":
        you = draw[opponent]
    else:
        you = wins_over[opponent]

    points += shape_points[you]
    points += match_result(opponent, you)

print("your points: %s" %points)
