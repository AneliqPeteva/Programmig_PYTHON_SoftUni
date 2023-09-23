string = input()
letter_position = list()

for position, letter in enumerate(string):
    if letter.isupper():
        letter_position.append(position)
print(letter_position)