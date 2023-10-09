text = input()
for letter in text:
    if letter.lower() not in ['a', 'o', 'u', 'e', 'i']:
        print(letter, end="")

