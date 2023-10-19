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
moving_target = [int(num) for num in input().split()]
command = input()

while command != "End":
    command = command.split()
    if command[0] == "Shoot":
        index = int(command[1])
        power = int(command[2])
        if 0 <= index < len(moving_target):
            moving_target[index] -= power
            if moving_target[index] <= 0:
                moving_target.pop(index)
    elif command[0] == "Add":
        index = int(command[1])
        value = int(command[2])
        if 0 <= index < len(moving_target):
            moving_target.insert(index, value)
        else:
            print("Invalid placement!")

    elif command[0] == "Strike":
        index = int(command[1])
        radius = int(command[2])
        start_index = index - radius
        end_index = index + radius
        if 0 <= start_index < len(moving_target) and 0 <= end_index < len(moving_target):
            for current_index in range(end_index, start_index - 1, -1):
                moving_target.pop(current_index)
        else:
            print("Strike missed!")
    command = input()

print(*moving_target, sep="|")

4.3