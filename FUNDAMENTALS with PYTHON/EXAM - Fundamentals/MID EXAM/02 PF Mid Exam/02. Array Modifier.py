list_numbers = list(map(int, input().split()))
command = input()

while command != "end":
    if "decrease" in command:
        list_numbers = [element - 1 for element in list_numbers]
        command = input()
        continue
    command, index_one, index_two = [x if x.isalpha() else int(x) for x in command.split()]
    if command == "swap":
        list_numbers[index_one], list_numbers[index_two] = list_numbers[index_two], list_numbers[index_one]

    elif command == "multiply":
        list_numbers[index_one] *= list_numbers[index_two]

    command = input()


print(*list_numbers, sep=", ")

