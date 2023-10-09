number = int(input())
wagons = [0] * number
command = input()
while command != "End":
    command = command.split()
    if command[0] == "add":
        wagons[-1] += int(command[1])
    elif command[0] == "insert":
        index = int(command[1])
        people = int(command[2])
        wagons[index] += people
    elif command[0] == "leave":
        index = int(command[1])
        people = int(command[2])
        wagons[index] -= people
    command = input()
print(wagons)
