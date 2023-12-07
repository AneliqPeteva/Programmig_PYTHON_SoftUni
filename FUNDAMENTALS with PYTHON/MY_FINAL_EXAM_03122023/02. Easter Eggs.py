import re

input_string = input()
while input_string:
    pattern = r"([@#]+([a-z]{3,})[@#]+[\D\W]*\/(\d+)\/+)"
    matches = re.finditer(pattern, input_string)

if matches:
    for match in matches:
        color = match.group(2)
        amount = match.group(3)
        if color.isalpha() and amount.isdigit():
            print(f"You found {amount} {color} eggs!")

# import re
#
# input_string = input()
#
# pattern = r"([@#]+([a-z]{3,})[@#]+[^A-Za-z0-9]*\/+(\d+)\/+)"
# matches = re.findall(pattern, input_string)
#
# if matches:
#     for match in matches:
#         print(f"You found {match[2]} {match[1]} eggs!")