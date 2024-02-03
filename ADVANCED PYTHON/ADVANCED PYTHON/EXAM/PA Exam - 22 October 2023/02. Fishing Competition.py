size = int(input())
matrix = []
amount = 0
my_position = []

directions = {
    "up": [-1, 0],
    "down": [1, 0],
    "left": [0, -1],
    "right": [0, 1],
}

for row in range(size):
    matrix.append(list(input()))

    if "S" in matrix[row]:
        my_position = [row, matrix[row].index("S")]
        # matrix[my_position[0]][my_position[1]] = "-"

command = input()

while command != "collect the nets":
    matrix[my_position[0]][my_position[1]] = "-"

    r, c = my_position[0] + directions[command][0], my_position[1] + directions[command][1]

    if not (0 <= r < size and 0 <= c < size):
        if r == size:
            r = 0
        elif r < 0:
            r = size - 1
        elif c == size:
            c = 0
        elif c < 0:
            c = size - 1
    element = matrix[r][c]
    if element == "-":
        my_position = [r, c]
        matrix[r][c] = "S"

    elif element.isdigit():
        amount += int(element)
        matrix[r][c] = "S"
        my_position = [r, c]


    elif element == "W":
        matrix[r][c] = "S"
        my_position = [r, c]
        amount = 0
        print(f"You fell into a whirlpool! The ship sank and you lost the fish you caught. Last coordinates of the ship: [{my_position[0]},{my_position[1]}]")
        exit()

    command = input()

if amount > 20:
    print("Success! You managed to reach the quota!")
else:
    print(f"You didn't catch enough fish and didn't reach the quota! You need {20 - amount} tons of fish more.")
if amount > 0:
    print(f"Amount of fish caught: {amount} tons.")
for row in matrix:
    print("".join(row))