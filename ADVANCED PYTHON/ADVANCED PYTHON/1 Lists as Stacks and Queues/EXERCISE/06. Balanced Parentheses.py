# from collections import deque
#
# parenthesis = deque(input())
# open_parenthesis = deque()
#
# while parenthesis:
#     current_parenthesis = parenthesis.popleft()
#
#     if current_parenthesis in "([{":
#         open_parenthesis.append(current_parenthesis)
#     elif not open_parenthesis:
#         print("NO")
#         break
#     else:
#         if f"{open_parenthesis.pop() + current_parenthesis}" not in "{}()[]":
#             print("NO")
#             break
#
# else:
#     print("YES")

expression = input()
stack = []
opening = {'{': '}', '[': ']', '(': ')'}

for char in expression:
    if char in opening:
        stack.append(char)
    elif char in opening.values():
        if not stack or opening[stack.pop()] != char:
            print("NO")
            break
else:
    print("YES")