rows, cols = [int(x) for x in input().split()]
neighborhood = []
start_position = []

directions = {
    "up": [-1, 0],
    "down": [1, 0],
    "left": [0, -1],
    "right": [0, 1],
}

for row in range(rows):
    line = list(input())
    neighborhood.append(line)

    if "B" in neighborhood[row]:
        start_position = [row, neighborhood[row].index("B")]

current_position = start_position
while True:
    command = input()

    current_row, current_col = current_position[0] + directions[command][0], current_position[1] + directions[command][1]


    if not (0 <= current_row < rows and 0 <= current_col < cols):
        neighborhood[start_position[0]][start_position[1]] = " "
        print("The delivery is late. Order is canceled.")
        break

    element = neighborhood[current_row][current_col]

    if element == "*":
        continue

    current_position = [current_row, current_col]

    if element == "P":
        neighborhood[current_row][current_col] = "R"
        print("Pizza is collected. 10 minutes for delivery.")

    elif element == "-":
        neighborhood[current_row][current_col] = "."
        continue

    elif element == "A":
        print("Pizza is delivered on time! Next order...")
        neighborhood[current_row][current_col] = "P"
        break


for row in neighborhood:
    print(f"{''.join(row)}")