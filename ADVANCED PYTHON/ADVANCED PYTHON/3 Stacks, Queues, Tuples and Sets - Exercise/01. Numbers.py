# first_line = set(int(x) for x in input().split())
# second_line = set(int(x) for x in input().split())
#
# function = {
#     "Add First": lambda x: [first_line.add(el) for el in x],
#     "Add Second": lambda x: [second_line.add(el) for el in x],
#     "Remove First": lambda x: [first_line.discard(el) for el in x],
#     "Remove Second": lambda x: [second_line.discard(el) for el in x],
#     "Check Subset": lambda: print(True) if first_line.issubset(second_line) or second_line.issubset(first_line) else print(False)
# }
# for com in range(int(input())):
#     first_command, *data = input().split()
#
#     command = first_command + " " + data.pop(0)
#
#     if data:
#         function[command]([int(x) for x in data])
#     else:
#         function[command]()
#
# print(*sorted(first_line), sep=", ")
# print(*sorted(second_line), sep=", ")


first_line = set(int(x) for x in input().split())
second_line = set(int(x) for x in input().split())

for com in range(int(input())):
    first_command, *data = input().split()

    command = first_command + " " + data.pop(0)

    if command == "Add First":
        [first_line.add(int(x)) for x in data]
    elif command == "Add Second":
        [second_line.add(int(x)) for x in data]
    elif command == "Remove First":
        [first_line.discard(int(x)) for x in data]
    elif command == "Remove Second":
        [second_line.discard(int(x)) for x in data]
    elif command == "Check Subset":
        if first_line.issubset(second_line) or second_line.issubset(first_line):
            print(True)
        else:
            print(False)

print(*sorted(first_line), sep=", ")
print(*sorted(second_line), sep=", ")
