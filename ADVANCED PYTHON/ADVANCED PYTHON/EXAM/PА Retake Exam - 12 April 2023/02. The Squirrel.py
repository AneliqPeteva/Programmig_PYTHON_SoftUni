size = int(input())
commands = input().split(", ")

goal_collect_hazelnuts = 3
hazelnuts_count = 0

matrix = []
position_squirrel = []

directions = {
    "up": [-1, 0],
    "down": [1, 0],
    "left": [0, -1],
    "right": [0, 1],
}

for row in range(size):
    line = list(input())
    matrix.append(line)

    if "s" in line:
        position_squirrel = [row, matrix[row].index("s")]
        matrix[position_squirrel[0]][position_squirrel[1]] = "*"


for current_com in commands:

    position_squirrel[0] += directions[current_com][0]
    position_squirrel[1] += directions[current_com][1]

    if not (0 <= position_squirrel[0] < size and 0 <= position_squirrel[1] < size):
        print("The squirrel is out of the field.")
        print(f"Hazelnuts collected: {hazelnuts_count}")
        exit()

    element = matrix[position_squirrel[0]][position_squirrel[1]]

    if element == "h":
        hazelnuts_count += 1
        if hazelnuts_count == 3:
            print("Good job! You have collected all hazelnuts!")
            print(f"Hazelnuts collected: {hazelnuts_count}")
            exit()

    elif element == "t":
        print("Unfortunately, the squirrel stepped on a trap...")
        print(f"Hazelnuts collected: {hazelnuts_count}")
        exit()

    matrix[position_squirrel[0]][position_squirrel[1]] = "*"

else:
    print("There are more hazelnuts to collect.")
    print(f"Hazelnuts collected: {hazelnuts_count}")


