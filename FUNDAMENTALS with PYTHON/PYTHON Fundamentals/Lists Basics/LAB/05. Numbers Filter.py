#number = int(input())
#numbers_list = []
#filtered_list = []
#for i in range(number):
#    current_number = int(input())
#    numbers_list.append(current_number)
#
#command = input()
#
#if command == "even":
#    for current_number in numbers_list:
#        if current_number % 2 == 0:
#            filtered_list.append(current_number)
#elif command == "odd":
#    for current_number in numbers_list:
#        if current_number % 2 != 0:
#            filtered_list.append(current_number)
#elif command == "negative":
#    for current_number in numbers_list:
#        if current_number < 0:
#            filtered_list.append(current_number)
#elif command == "positive":
#    for current_number in numbers_list:
#        if current_number >= 0:
#            filtered_list.append(current_number)
#
#print(filtered_list)


n = int(input())
COMMAND_EVEN = 'even'
COMMAND_ODD = 'odd'
COMMAND_NEGATIVE = 'negative'
COMMAND_POSITIVE = 'positive'

numbers = [int(input()) for _ in range(n)]

filtered_numbers = []

command = input()

for num in numbers:
    filter_command = (
        (command == COMMAND_EVEN and num % 2 == 0) or
        (command == COMMAND_ODD and num % 2 != 0) or
        (command == COMMAND_POSITIVE and num >= 0) or
        (command == COMMAND_NEGATIVE and num < 0)
        )

    if filter_command:
        filtered_numbers.append(num)

print(filtered_numbers)