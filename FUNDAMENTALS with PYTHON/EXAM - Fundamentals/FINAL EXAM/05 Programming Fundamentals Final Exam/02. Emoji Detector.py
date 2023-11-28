
import re

string = input()
cool_threshold_sum = 1
emoji_is_cool = []
pattern_digit = r"\d"
match_digit = re.findall(pattern_digit, string)
for current_digit in match_digit:
    cool_threshold_sum *= int(current_digit)

pattern_emoji = r"::[A-Z][a-z]{2,}::|\*\*[A-Z][a-z]{2,}\*\*"
match_emoji = re.findall(pattern_emoji, string)
for current_emoji in match_emoji:
    total_ascii_letter = 0
    for letter in current_emoji:
        if letter.isalpha():
            total_ascii_letter += ord(letter)
    if total_ascii_letter >= cool_threshold_sum:
        emoji_is_cool.append(current_emoji)

print(f"Cool threshold: {cool_threshold_sum}")
print(f"{len(match_emoji)} emojis found in the text. The cool ones are:")
for cool_emoji in emoji_is_cool:
    print(cool_emoji)


# import re
#
# text = input()
# pattern = r'([:]{2}|[*]{2})([A-Z]{1}[a-z]{2,})(\1)'
# matches = re.findall(pattern, text)
#
# threshold = 1
# for char in text:
#     if char.isdigit():
#         threshold *= int(char)
#
# cool_emojis = []
# for emoji in matches:
#     coolnes = 0
#     for char in emoji[1]:
#         coolnes += ord(char)
#
#     if coolnes > threshold:
#         cool_emojis.append(emoji)
#
# print(f'Cool threshold: {threshold}')
# if len(matches) > 0:
#     print(f'{len(matches)} emojis found in the text. The cool ones are:')
#     for emoji in cool_emojis:
#         print(''.join(emoji))