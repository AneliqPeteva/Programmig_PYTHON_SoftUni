start_index_character = int(input())
end_index_character = int(input())
output = ""
for character in range(start_index_character, end_index_character +1):
    char = chr(character)
    print(char, end=" ")