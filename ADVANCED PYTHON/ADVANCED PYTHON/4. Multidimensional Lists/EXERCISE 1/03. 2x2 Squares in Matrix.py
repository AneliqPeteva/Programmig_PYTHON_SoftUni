rows, columns = [int(x) for x in input().split()]
matrix = [input().split() for row in range(rows)]

equal_block = 0

for row in range(rows - 1):
    for column in range(columns - 1):
        symbol = matrix[row][column]

        if matrix[row][column + 1] == symbol and matrix[row + 1][column] == symbol and matrix[row + 1][column + 1] == symbol:
            equal_block += 1
print(equal_block)