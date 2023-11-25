import re

pattern = r"(w{3}\.[A-Za-z0-9\-\.]+\.[a-z]+)"
line = input()
while line:
    match = re.search(pattern, line)
    if match:
        valid_url = match.group(1)
        print(valid_url)
    line = input()

# import re
#
# while True:
#     line = input()
#
#     if not line:
#         break
#     pattern = r"www\.[A-Za-z0-9]+([\-][A-Za-z0-9]+)*(\.[a-z]+)(\.[a-z]+)*"
#
#     matches = re.finditer(pattern, line)
#     for match in matches:
#         print(match[0])