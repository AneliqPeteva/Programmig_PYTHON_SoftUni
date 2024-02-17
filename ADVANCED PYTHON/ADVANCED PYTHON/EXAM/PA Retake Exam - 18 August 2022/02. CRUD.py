ROWS, COLS = 6, 6
matrix = []
for row in range(ROWS):
    line = input().split()
    matrix.append(line)

position = input()
my_position = [int(position[1]), int(position[4])]

directions = {
    "up": [-1, 0],
    "down": [1, 0],
    "left": [0, -1],
    "right": [0, 1],
}

while True:
    command = input().split(", ")

    if command[0] == 'Stop':
        break

    if command[0] == 'Create':
        current_direction = command[1]
        value = command[2]

        current_r = my_position[0] + directions[current_direction][0]
        current_c = my_position[1] + directions[current_direction][1]
        if matrix[current_r][current_c] == ".":
            matrix[current_r][current_c] = value

    elif command[0] == 'Update':
        current_direction = command[1]
        value = command[2]

        current_r = my_position[0] + directions[current_direction][0]
        current_c = my_position[1] + directions[current_direction][1]
        if matrix[current_r][current_c] != ".":
            matrix[current_r][current_c] = value


    elif command[0] == 'Delete':
        current_direction = command[1]

        current_r = my_position[0] + directions[current_direction][0]
        current_c = my_position[1] + directions[current_direction][1]
        if matrix[current_r][current_c] != ".":
            matrix[current_r][current_c] = "."
    elif command[0] == 'Read':
        current_direction = command[1]

        current_r = my_position[0] + directions[current_direction][0]
        current_c = my_position[1] + directions[current_direction][1]
        if matrix[current_r][current_c] != ".":
            print(matrix[current_r][current_c])

    my_position = [current_r, current_c]

for row in matrix:
    print(*row, sep=" ")

