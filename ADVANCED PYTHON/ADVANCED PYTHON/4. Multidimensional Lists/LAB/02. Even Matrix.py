# number = int(input())
#
# matrix_even = []
#
# for _ in range(number):
#     current_list = []
#     number_list = input().split(", ")
#     for num in number_list:
#         if int(num) % 2 == 0:
#             current_list.append(int(num))
#
#
#     matrix_even.append(current_list)
#
# print(matrix_even)


matrix_even = []

for _ in range(int(input())):
    current_list = [int(x) for x in input().split(", ") if int(x) % 2 == 0]
    matrix_even.append(current_list)

print(matrix_even)