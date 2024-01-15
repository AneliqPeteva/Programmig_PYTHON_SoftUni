# matrix = []
# flattening_matrix = []
# for _ in range(int(input())):
#     current_list = [int(x) for x in input().split(", ")]
#     matrix.append(current_list)
#
# for current_ind in range(len(matrix)):
#     for index in range(len(matrix[current_ind])):
#         element = int(matrix[current_ind][index])
#         flattening_matrix.append(element)
#
#
#
# print(flattening_matrix)




# matrix = []
# flattening_matrix = []
# for _ in range(int(input())):
#     current_list = [int(x) for x in input().split(", ")]
#     matrix.append(current_list)
# for list_el in matrix:
#     flattening_matrix.extend(list_el)
#
# print(flattening_matrix)


matrix = []

for _ in range(int(input())):
    current_list = [int(x) for x in input().split(", ")]
    matrix.append(current_list)
flattening_matrix = [el for list_el in matrix for el in list_el]
print(flattening_matrix)