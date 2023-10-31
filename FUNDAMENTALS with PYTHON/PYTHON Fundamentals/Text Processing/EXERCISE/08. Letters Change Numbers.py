# text = input().split()
# total_sum = 0
#
#
# for element in text:
#     letter = ""
#     digit = ""
#     for current_letter in element:
#         if current_letter.isalpha():
#             letter += current_letter
#         elif current_letter.isdigit():
#             digit += current_letter
#     if letter[0].isupper():
#         value_letter = ord(letter[0]) - 64
#         total_sum += int(digit) / value_letter
#     else:
#         value_letter = ord(letter[0]) - 96
#         total_sum += int(digit) * value_letter
#     if letter[-1].isupper():
#         value_letter = ord(letter[-1]) - 64
#         total_sum -= value_letter
#     else:
#         value_letter = ord(letter[-1]) - 96
#         total_sum += value_letter
#
# print(f"{total_sum:.2f}")


text = input().split()
total_sum = 0

for current_string in text:
    first_letter = current_string[0]
    last_letter = current_string[-1]
    number = int(current_string[1:len(current_string) - 1])
    if first_letter.isupper():
        first_letter_position = ord(first_letter) - 64
        total_sum += number / first_letter_position
    elif first_letter.islower():
        first_letter_position = ord(first_letter) - 96
        total_sum += number * first_letter_position

    if last_letter.isupper():
        last_letter_position = ord(last_letter) - 64
        total_sum -= last_letter_position
    elif last_letter.islower():
        last_letter_position = ord(last_letter) - 96
        total_sum += last_letter_position

print(f"{total_sum:.2f}")