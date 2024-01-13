row, columns =[int(element) for element in input().split(", ")]
matrix = []
total_sum = 0

for _ in range(row):
    current_list = [int(element) for element in input().split(", ")]
    total_sum += sum(el for el in current_list)
    matrix.append(current_list)

print(total_sum)
print(matrix)