names_of_the_coffee = input().split()
numbers = int(input())

for current_num in range(numbers):
    command = input().split()
    if command[0] == "Include":
        names_of_the_coffee.append(command[1])
    elif command[0] == "Remove":
        number_of_coffee = int(command[2])
        if command[1] == "first":
            names_of_the_coffee = names_of_the_coffee[number_of_coffee:]
        elif command[1] == "last":
            names_of_the_coffee = names_of_the_coffee[:-number_of_coffee]
    elif command[0] == "Prefer":
        coffee_index_1 = int(command[1])
        coffee_index_2 = int(command[2])
        if 0 <= coffee_index_1 < len(names_of_the_coffee) and 0 <= coffee_index_2 < len(names_of_the_coffee):
            names_of_the_coffee[coffee_index_1], names_of_the_coffee[coffee_index_2] = names_of_the_coffee[coffee_index_2], names_of_the_coffee[coffee_index_1]

    elif command[0] == "Reverse":
        names_of_the_coffee.reverse()

print("Coffees:")
print(*names_of_the_coffee)
