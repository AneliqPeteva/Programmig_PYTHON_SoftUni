rows, cols = [int(x) for x in input().split(',')]
cupboard = []
mouse_pos = []
all_cheese = 0

directions = {
    "up": [-1, 0],
    "down": [1, 0],
    "left": [0, -1],
    "right": [0, 1],
}

for row in range(rows):
    line = list(input())
    cupboard.append(line)

    if "M" in line:
        mouse_pos = [row, cupboard[row].index("M")]

    all_cheese += line.count("C")



while all_cheese != 0:
    command = input()
    if command == "danger":
        print("Mouse will come back later!")
        break

    next_row = mouse_pos[0] + directions[command][0]
    next_col = mouse_pos[1] + directions[command][1]

    if not (0 <= next_row < rows and 0 <= next_col < cols):
        print("No more cheese for tonight!")
        break
    if cupboard[next_row][next_col] == "@":
        continue
    # else:
    #     cupboard[mouse_pos[0]][mouse_pos[1]] = "*"
    #     mouse_pos = [next_row, next_col]

    element = cupboard[next_row][next_col]

    if element == "T":
        cupboard[mouse_pos[0]][mouse_pos[1]] = "*"
        mouse_pos = [next_row, next_col]
        cupboard[mouse_pos[0]][mouse_pos[1]] = "M"
        print("Mouse is trapped!")
        break

    if element == "C":
        all_cheese -= 1
        cupboard[mouse_pos[0]][mouse_pos[1]] = "*"
        mouse_pos = [next_row, next_col]
        cupboard[mouse_pos[0]][mouse_pos[1]] = "M"

    if element == "*":
        cupboard[mouse_pos[0]][mouse_pos[1]] = "*"
        mouse_pos = [next_row, next_col]
        cupboard[mouse_pos[0]][mouse_pos[1]] = "M"
        continue



else:
    print("Happy mouse! All the cheese is eaten, good night!")
for row in cupboard:
    print(*row, sep= "")