SIZE = int(input())
matrix = []
my_positions = []
armor = 300 # bronq
count_enemy_aircraft = 4 #vrajeski_iztrebitelq
directions = {
    "up": [-1, 0],
    "down": [1, 0],
    "left": [0, -1],
    "right": [0, 1],
}

for row in range(SIZE):
    line = list(input())
    matrix.append(line)

    if "J" in line:
        my_positions = [row, matrix[row].index("J")]
        matrix[my_positions[0]][my_positions[1]] = "-"

while True:
    command = input()

    current_row, current_col = my_positions[0] + directions[command][0], my_positions[1] + directions[command][1]
    my_positions = [current_row, current_col]
    if matrix[current_row][current_col] == "-":
        continue

    elif matrix[current_row][current_col] == "E":
        count_enemy_aircraft -= 1
        if count_enemy_aircraft == 0:
            print(f"Mission accomplished, you neutralized the aerial threat!")
            matrix[my_positions[0]][my_positions[1]] = "J"
            break
        else:
            armor -= 100
            if armor <= 0:
                print(f"Mission failed, your jetfighter was shot down! Last coordinates [{current_row}, {current_col}]!")
                matrix[my_positions[0]][my_positions[1]] = "J"
                break



    elif matrix[current_row][current_col] == "R":
        armor = 300

    matrix[my_positions[0]][my_positions[1]] = "-"

for row in matrix:
    print(*row, sep="")



