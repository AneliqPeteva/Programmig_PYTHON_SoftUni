import re

text = input()

pattern = r"(^|(?<=\s))([A-Za-z0-9])+([\.\-\_][A-Za-z0-9]+)*@([A-Za-z-]+)\.([A-Za-z-]+)([\.A-Za-z-])*(\b|(?=\s))"

matches = re.finditer(pattern, text)

for match in matches:
    print(match[0])
