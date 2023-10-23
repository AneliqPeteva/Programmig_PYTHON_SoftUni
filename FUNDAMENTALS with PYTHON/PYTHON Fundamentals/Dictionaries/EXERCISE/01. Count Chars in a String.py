symbols= [char for char in input() if char != " "]
letters = {}

for symbol in symbols:
    if symbol not in letters.keys():
        letters[symbol] = 0
    letters[symbol] += 1
for character, occurrences in letters.items():
    print(f"{character} -> {occurrences}")
        