data = input().split(', ')
rows = int(data[0])
cols = int(data[1])

matrix = []

for row in range(rows):
    element = [int(el) for el in input().split(', ')]
    matrix.append(element)
max_sum = 0
max_aum_sub_matrix = []
for row_ind in range(rows - 1):
    for col_ind in range(cols - 1):
        current_element = matrix[row_ind][col_ind]
        next_element = matrix[row_ind][col_ind + 1]
        element_below = matrix[row_ind + 1][col_ind]
        element_diagonal = matrix[row_ind + 1][col_ind + 1]
        sum_element = current_element + element_below + next_element + element_diagonal

        if max_sum < sum_element:
            max_sum = sum_element
            max_aum_sub_matrix = [
                [current_element, next_element],
                [element_below, element_diagonal]
            ]

print(*max_aum_sub_matrix[0])
print(*max_aum_sub_matrix[1])
print(max_sum)
