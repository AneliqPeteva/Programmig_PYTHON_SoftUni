import re

text = input()

pattern = r"\b_([A-Za-z\d]+)\b"

matches = re.findall(pattern, text)

print(",".join(matches))