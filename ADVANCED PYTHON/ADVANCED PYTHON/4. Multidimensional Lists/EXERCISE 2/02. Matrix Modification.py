num = int(input())
matrix = [[int(n) for n in input().split()] for row in range(num)]

command = input().split()



while command[0] != "END":

    type_command, row_index, col_index, value = command[0], int(command[1]), int(command[2]), int(command[3])

    if 0 <= row_index < num and 0 <= col_index < num:
        if type_command == "Add":
            matrix[row_index][col_index] += value
        elif type_command == "Subtract":
            matrix[row_index][col_index] -= value
    else:
        print("Invalid coordinates")

    command = input().split()

[print(*row) for row in matrix]
