import re

text = input()
search_word = input()

pattern = fr"\b{search_word}\b"

matches = re.findall(pattern, text, re.IGNORECASE)

print(len(matches))