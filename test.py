# #2.3 MID EXAM
# numbers_list = [int(numb) for numb in input().split()]
# top_of_numbers = 5
# greater_than_the_average_value = []
#
#
# average_number = sum(numbers_list)/len(numbers_list)
#
# for current_number in numbers_list:
#     if current_number > average_number:
#         greater_than_the_average_value.append(current_number)
#         # top_of_numbers -= 1
#         # if top_of_numbers == 0:
#         #     break
# sort_numbers = sorted(greater_than_the_average_value, reverse=True)
# if len(greater_than_the_average_value) == 0:
#     print("No")
# else:
#     print(*sort_numbers[:top_of_numbers])

#3.3
# moving_target = [int(num) for num in input().split()]
# command = input()
#
# while command != "End":
#     command = command.split()
#     if command[0] == "Shoot":
#         index = int(command[1])
#         power = int(command[2])
#         if 0 <= index < len(moving_target):
#             moving_target[index] -= power
#             if moving_target[index] <= 0:
#                 moving_target.pop(index)
#     elif command[0] == "Add":
#         index = int(command[1])
#         value = int(command[2])
#         if 0 <= index < len(moving_target):
#             moving_target.insert(index, value)
#         else:
#             print("Invalid placement!")
#
#     elif command[0] == "Strike":
#         index = int(command[1])
#         radius = int(command[2])
#         start_index = index - radius
#         end_index = index + radius
#         if 0 <= start_index < len(moving_target) and 0 <= end_index < len(moving_target):
#             for current_index in range(end_index, start_index - 1, -1):
#                 moving_target.pop(current_index)
#         else:
#             print("Strike missed!")
#     command = input()
#
# print(*moving_target, sep="|")

# 4.3
house_of_neighbors = [int(num) for num in input().split("@")]
input_line = input()
start_index = 0
current_index = 0
while input_line != "Love!":
    jump = input_line.split()
    index = int(jump[1])
    current_index += index
    if current_index not in range(len(house_of_neighbors)):
        current_index = 0
    if house_of_neighbors[current_index] >= 2:
        house_of_neighbors[current_index] -= 2
        if house_of_neighbors[current_index] == 0:
            print(f"Place {current_index} has Valentine's day.")
    elif house_of_neighbors[current_index] == 0:
        print(f"Place {current_index} already had Valentine's day.")

    input_line = input()

print(f"Cupid's last position was {current_index}.")
if sum(house_of_neighbors) == 0:
    print(f"Mission was successful.")
else:
    count_house = 0
    for house in house_of_neighbors:
        if house != 0:
            count_house += 1
    print(f"Cupid has failed {count_house} places.")