list_with_groceries = input().split("!")
command = input()

while command != "Go Shopping!":
    command = command.split()
    if command[0] == "Urgent":
        if command[1] not in list_with_groceries:
            list_with_groceries.insert(0, command[1])
    elif command[0] == "Unnecessary":
        if command[1] in list_with_groceries:
            list_with_groceries.remove(command[1])
    elif command[0] == "Correct":
        if command[1] in list_with_groceries:
            list_with_groceries[list_with_groceries.index(command[1])] = command[2]
    elif command[0] == "Rearrange":
        if command[1] in list_with_groceries:
            list_with_groceries.remove(command[1])
            list_with_groceries.append(command[1])
    command = input()

print(", ".join(list_with_groceries))


