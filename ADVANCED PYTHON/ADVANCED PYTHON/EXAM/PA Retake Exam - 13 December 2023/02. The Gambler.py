size = int(input())
matrix = []
amount = 100
gamer_position = []

directions = {
    "up": [-1, 0],
    "down": [1, 0],
    "left": [0, -1],
    "right": [0, 1],
}

for row in range(size):
    matrix.append(list(input()))

    if "G" in matrix[row]:
        gamer_position = [row, matrix[row].index("G")]

command = input()

while command != "end":

    r, c = gamer_position[0] + directions[command][0], gamer_position[1] + directions[command][1]

    if not (0 <= r < size and 0 <= c < size):
        print("Game over! You lost everything!")
        break

    matrix[gamer_position[0]][gamer_position[1]] = "-"
    gamer_position = [r, c]

    if matrix[r][c] == "-":
        matrix[r][c] = "G"
        command = input()
        continue
    elif matrix[r][c] == "W":
        matrix[r][c] = "G"
        amount += 100
    elif matrix[r][c] == "P":
        matrix[r][c] = "G"
        amount -= 200
        if amount <= 0:
            print("Game over! You lost everything!")
            break
    elif matrix[r][c] == "J":
        matrix[r][c] = "G"
        amount += 100000
        print(f"You win the Jackpot!\nEnd of the game. Total amount: {amount}$")
        for row in matrix:
            print(''.join(row))
        break

    matrix[r][c] = "G"

    command = input()

else:
    print(f"End of the game. Total amount: {amount}$")
    for row in matrix:
        print(''.join(row))
