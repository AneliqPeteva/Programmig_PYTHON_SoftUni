n = int(input())
matrix = []

for row in range(n):
    elements = [int(el) for el in input().split()]
    matrix.append(elements)
sum_diagonal = 0

for row_index in range(n):
    sum_diagonal += matrix[row_index][row_index]
print(sum_diagonal)