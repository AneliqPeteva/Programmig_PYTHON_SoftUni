list_of_characters = input().split(", ")
dict_of_characters = {letter: ord(letter) for letter in list_of_characters}
print(dict_of_characters)
