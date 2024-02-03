rows, cols = [int(x) for x in input().split(" ")]
matrix = []
start_position = []

directions = {
    "up": [-1, 0],
    "down": [1, 0],
    "left": [0, -1],
    "right": [0, 1],
}

for row in range(rows):
    matrix.append(list(input()))

    if "B" in matrix[row]:
        start_position = [row, matrix[row].index("B")]
        current_position = [start_position[0], start_position[1]]


command = input()

while command:
    current_row, current_col = current_position[0] + directions[command][0], current_position[1] + directions[command][1]


    if not (0 <= current_row < rows and 0 <= current_col < cols):
        print("The delivery is late. Order is canceled.")
        matrix[start_position[0]][start_position[1]] = " "
        [print(*row, sep="") for row in matrix]
        exit()

    element = matrix[current_row][current_col]

    if element == "P":
        current_position = [current_row, current_col]
        matrix[current_row][current_col] = "R"
        print("Pizza is collected. 10 minutes for delivery.")

    elif element == "*":
        command = input()
        continue

    elif element == "A":
        current_position = [current_row, current_col]
        matrix[current_row][current_col] = "P"
        print("Pizza is delivered on time! Next order...")
        [print(*row, sep="") for row in matrix]

    if element == "-":
        current_position = [current_row, current_col]
        matrix[current_row][current_col] = "."



    command = input()


66 % judge

