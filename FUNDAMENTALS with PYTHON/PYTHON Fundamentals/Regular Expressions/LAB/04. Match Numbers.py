import re

number = input()
pattern = r'(^|(?<=\s))-?([0]|[1-9][0-9]*)(\.\d+)?($|(?=\s))'
matches = re.finditer(pattern, number)

for match in matches:
    print(match.group(), end=" ")
