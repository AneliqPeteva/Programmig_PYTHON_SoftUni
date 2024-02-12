SIZE = int(input())
racing_number = input()

matrix = []
tunnels_positions = []
start_positions = [0, 0]
kilometers = 0

directions = {
    "up": [-1, 0],
    "down": [1, 0],
    "left": [0, -1],
    "right": [0, 1],
}

for row in range(SIZE):
    line = input().split()
    matrix.append(line)

    if "T" in line:
        tunnels_positions.append(row)
        tunnels_positions.append(matrix[row].index("T"))

while True:
    tunnels_positions_1 = [tunnels_positions[0], tunnels_positions[1]]
    tunnels_positions_2 = [tunnels_positions[2], tunnels_positions[3]]
    command = input()

    if command == "End":
        print(f"Racing car {racing_number} DNF.")
        break

    start_positions[0] = start_positions[0] + directions[command][0]
    start_positions[1] = start_positions[1] + directions[command][1]

    element = matrix[start_positions[0]][start_positions[1]]

    if element == "T":
        if start_positions == tunnels_positions_1:
            start_positions = tunnels_positions_2
        else:
            start_positions = tunnels_positions_1
        kilometers += 30
        matrix[tunnels_positions_1[0]][tunnels_positions_1[1]] = "."
        matrix[tunnels_positions_2[0]][tunnels_positions_2[1]] = "."

    elif element == "F":
        kilometers += 10
        print(f"Racing car {racing_number} finished the stage!")
        break

    elif element == ".":
        kilometers += 10


matrix[start_positions[0]][start_positions[1]] = "C"
print(f"Distance covered {kilometers} km.")
for row in matrix:
    print(*row, sep= "")






