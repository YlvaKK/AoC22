draw = { "A": "X", "B": "Y", "C": "Z" }
wins_over = { "C": "X", "A": "Y", "B": "Z" }
loses_to = { "B": "X", "C": "Y", "A": "Z" }

shape_points = { "X": 1, "Y": 2, "Z": 3 }
points = 0

f = open('2/day_two_input')
lines = f.readlines()

for line in lines:
    shapes = line.split(" ")
    opponent, outcome = shapes[0].strip(), shapes[1].strip()

    if outcome == "X":
        you = loses_to[opponent]
    elif outcome == "Y":
        you = draw[opponent]
        points += 3
    else:
        you = wins_over[opponent]
        points += 6

    points += shape_points[you]

print("your points: %s" %points)