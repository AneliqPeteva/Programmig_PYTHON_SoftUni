sequance_of_strings = input().split()
result = []
for current_word in sequance_of_strings:
    length = len(current_word)
    result += current_word * length

print("".join(result))


# sequance_of_strings = input().split()
# result = [text * len(text) for text in sequance_of_strings]
#
# print("".join(result))