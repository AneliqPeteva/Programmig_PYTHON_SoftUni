num = int(input())
matrix = [[int(n) for n in input().split()] for row in range(num)]
primary_sum = 0
secondary_sum = 0

for i in range(num):
    primary_sum += matrix[i][i]
    secondary_sum += matrix[i][num - i -1]

print(f"{abs(primary_sum - secondary_sum)}")

# rows = int(input())
#
# matrix = [[int(x) for x in input().split(' ')] for _ in range(rows)]
# primary = [matrix[row][row] for row in range(len(matrix))]
# secondary = [matrix[row][rows - row  - 1] for row in range(len(matrix))]
# sum_primary = sum(primary)
# sum_secondary = sum(secondary)
# print(f"{abs(sum_primary - sum_secondary)}")