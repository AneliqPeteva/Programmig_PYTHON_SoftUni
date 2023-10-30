text = input()

final_text = ""
last_character = ""

for current_character in text:
    if current_character != last_character:
        final_text += current_character
        last_character = current_character

print(final_text)