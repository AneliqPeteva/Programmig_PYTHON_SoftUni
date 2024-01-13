# text = input()
#
# for letter in sorted(set(text)):
#     print(f"{letter}: {text.count(letter)} time/s")


occurrences = {}

for letter in input():
    occurrences[letter] = occurrences.get(letter, 0) + 1

for letter, count in sorted(occurrences.items()):
    print(f"{letter}: {count} time/s")