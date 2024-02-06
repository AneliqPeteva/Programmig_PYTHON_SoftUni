rows, cols = [int(x) for x in input().split()]
playground = []
my_position = []
moves = 0
touched_opponents_count = 0
opponents = 3

directions = {
    "up": [-1, 0],
    "down": [1, 0],
    "left": [0, -1],
    "right": [0, 1],
}


for row in range(rows):
    line = input().split(" ")
    playground.append(line)

    if "B" in playground[row]:
        my_position = [row, playground[row].index("B")]
        playground[my_position[0]][my_position[1]] = "-"

while True:
    command = input()
    if command == "Finish":
        break

    current_row, current_col = my_position[0] + directions[command][0], my_position[1] + directions[command][1]

    if not 0 <= current_row < rows and 0 <= current_col < cols:
        continue

    elif playground[current_row][current_col] == "O":
        continue


    if playground[current_row][current_col] == "P":
        my_position = [current_row, current_col]
        playground[my_position[0]][my_position[1]] = "-"
        touched_opponents_count += 1
        moves += 1

        if touched_opponents_count == opponents:
            break

    elif playground[current_row][current_col] == "-":
        my_position = [current_row, current_col]
        moves += 1


print(f"Game over!\nTouched opponents: {touched_opponents_count} Moves made: {moves}")

