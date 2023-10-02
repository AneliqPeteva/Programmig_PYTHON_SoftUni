def all_characters(first, second):
    characters = []
    for current_char in range(ord(first) + 1, ord(second)):
        characters.append(chr(current_char))
    return characters


first_character = input()
second_character = input()
result = all_characters(first_character, second_character)
print(*result)