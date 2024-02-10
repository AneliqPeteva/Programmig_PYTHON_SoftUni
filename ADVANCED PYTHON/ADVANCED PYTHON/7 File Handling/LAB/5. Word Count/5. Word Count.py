import re

with open("words.txt", "r") as file:
    searched_words = file.read().split()

with open("input.txt", "r") as file:
    text = file.read().lower()

words = {}
for searched_word in searched_words:
    pattern = rf"\b{searched_word}\b"
    result = re.findall(pattern, text)
    words[searched_word] = len(result)

with open("output.txt", "w") as file:
    for word, quantity in sorted(words.items(), key=lambda kvp: -(kvp[1])):
        file.write(f"{word} - {quantity}\n")