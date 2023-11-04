number = int(input())
for num in range(number):
    text = input()
    name = text[text.index("@") + 1: text.index("|")]
    age = text[text.index("#") + 1: text.index("*")]
    print(f"{name} is {age} years old.")




# number = int(input())
# for num in range(number):
#     name = ""
#     age = ""
#     text = input()
#     for index in range(len(text)):
#         if text[index] == "@":
#             for letter_name_index in range(index + 1, len(text)):
#                 if text[letter_name_index] != "|":
#                     name += text[letter_name_index]
#                 else:
#                     break
#         elif text[index] == "#":
#             for letter_age_index in range(index + 1, len(text)):
#                 if text[letter_age_index] != "*":
#                     age += text[letter_age_index]
#                 else:
#                     break
#     print(f"{name} is {age} years old.")
