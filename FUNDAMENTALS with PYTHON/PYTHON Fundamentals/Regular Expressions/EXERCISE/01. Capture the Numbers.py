import re


pattern = re.compile(r"\d+")
while True:
    data = input()
    if data:
        matches = pattern.finditer(data)

        for match in matches:
            print(match[0], end=" ")
    else:
        break


