# from collections import deque
# numbers = deque()
#
# map_functions = {
#     1: lambda x: numbers.append(x[1]),
#     2: lambda x: numbers.pop() if numbers else None,
#     3: lambda x: print(max(numbers)) if numbers else None,
#     4: lambda x: print(min(numbers)) if numbers else None,
# }
#
# for element in range(int(input())):
#     number_data = [int(x) for x in input().split()]
#     map_functions[number_data[0]](number_data)
#
# numbers.reverse()
# print(*numbers, sep=", ")

stack = []
count = int(input())

for current_count in range(count):
    command = input().split()
    if command[0] == '1':
        number = int(command[1])
        stack.append(number)
    elif command[0] == '2':
        if len(stack) != 0:
            stack.pop()
    elif command[0] == '3':
        if len(stack) != 0:
            print(f"{max(stack)}")
    elif command[0] == '4':
        if len(stack) != 0:
            print(f"{min(stack)}")
if len(stack):
    print(", ".join(str(stack.pop()) for n in range(len(stack))))