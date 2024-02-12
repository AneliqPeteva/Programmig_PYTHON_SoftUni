SIZE = int(input())

matrix = []
my_position = []
mines_count = 0
battle_cruiser_count = 0

directions = {
    "up": [-1, 0],
    "down": [1, 0],
    "left": [0, -1],
    "right": [0, 1],
}

for row in range(SIZE):
    line = list(input())
    matrix.append(line)
    if "S" in line:
        my_position = [row, matrix[row].index("S")]
        matrix[my_position[0]][my_position[1]] = "-"

while True:
    command = input()
    current_row = my_position[0] + directions[command][0]
    current_col = my_position[1] + directions[command][1]

    my_position = [current_row, current_col]
    element = matrix[current_row][current_col]

    if element == "-":
        continue
    elif element == "*":
        matrix[my_position[0]][my_position[1]] = "-"
        mines_count += 1
        if mines_count == 3:
            matrix[my_position[0]][my_position[1]] = "S"
            print(f"Mission failed, U-9 disappeared! Last known coordinates [{my_position[0]}, {my_position[1]}]!")
            break
    elif element == "C":
        matrix[my_position[0]][my_position[1]] = "-"
        battle_cruiser_count += 1
        if battle_cruiser_count == 3:
            matrix[my_position[0]][my_position[1]] = "S"
            print("Mission accomplished, U-9 has destroyed all battle cruisers of the enemy!")
            break

for row in matrix:
    print(*row, sep="")


