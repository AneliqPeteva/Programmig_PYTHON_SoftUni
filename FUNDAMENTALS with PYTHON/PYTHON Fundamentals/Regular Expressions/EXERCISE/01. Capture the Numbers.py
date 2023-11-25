import re

line = input()
while line:
    pattern = "\d+"
    matches = re.findall(pattern, line)
    if matches:
        print(" ".join(matches), end=" ")
    line = input()

# import re
#
#
# pattern = re.compile(r"\d+")
# while True:
#     data = input()
#     if data:
#         matches = pattern.finditer(data)
#
#         for match in matches:
#             print(match[0], end=" ")
#     else:
#         break


