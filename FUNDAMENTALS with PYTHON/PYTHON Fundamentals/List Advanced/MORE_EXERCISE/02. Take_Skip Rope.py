text = [input()]
list_letter, list_digit = [], []
output = []
for word in text:
    for letter in word:
        if letter.isdigit():
            list_digit.append(letter)
        else:
            list_letter.append(letter)
for current_element in range(0, len(list_digit), 2):
    take, skip = list_digit[current_element], list_digit[current_element + 1]
    output += list_letter[:int(take)]
    list_letter = list_letter[int(take) + int(skip):]

print(*output, sep="")
