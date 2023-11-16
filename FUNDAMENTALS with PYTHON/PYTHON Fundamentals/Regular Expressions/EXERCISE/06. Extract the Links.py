import re

while True:
    line = input()

    if not line:
        break
    pattern = r"www\.[A-Za-z0-9]+([\-][A-Za-z0-9]+)*(\.[a-z]+)(\.[a-z]+)*"

    matches = re.finditer(pattern, line)
    for match in matches:
        print(match[0])