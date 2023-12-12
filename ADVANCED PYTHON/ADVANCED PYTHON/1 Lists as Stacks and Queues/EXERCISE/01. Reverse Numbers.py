# input_data = input().split()
#
# while input_data:
#     print(input_data.pop(), end=" ")

input_data = input().split()

for element in range(len(input_data)):
    print(f'{input_data.pop()}', end=" ")