import re

number = input()
pattern = "\\+359 2 \d{3} \d{4}|\+359-2-\d{3}-\d{4}\\b"
matches = re.findall(pattern, number)

print(", ".join(matches))