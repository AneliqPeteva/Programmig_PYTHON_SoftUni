rows = int(input())

matrix = [[int(x) for x in input().split(', ')] for _ in range(rows)]
primary = [matrix[row][row] for row in range(len(matrix))]
secondary = [matrix[row][rows - row  - 1] for row in range(len(matrix))]
print(f"Primary diagonal: {', '.join([str(x) for x in primary])}. Sum: {sum(primary)}")
print(f"Secondary diagonal: {', '.join([str(x) for x in secondary])}. Sum: {sum(secondary)}")