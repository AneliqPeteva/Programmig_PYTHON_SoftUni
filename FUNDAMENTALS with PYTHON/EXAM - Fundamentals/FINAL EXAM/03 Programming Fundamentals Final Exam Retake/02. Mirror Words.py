import re


text_string = input()
mirror_word = []
pattern = r"([@#])([A-Za-z]{3,})\1\1([A-Za-z]{3,})\1"

match = re.findall(pattern, text_string)
if len(match) <= 0:
    print("No word pairs found!")
else:
    valid_pairs_count = len(match)
    print(f"{valid_pairs_count} word pairs found!")
    for words in match:
        word_one = words[1]
        word_two = words[2]
        if word_one == word_two[::-1]:
            mirror_word.append(f"{word_one} <=> {word_two}")

if len(mirror_word) > 0:
    print("The mirror words are:")
    print(*mirror_word, sep=", ")
else:
    print("No mirror words!")