# Read user input
input_text = input()
total = 0
length_text = len(input_text)
# Logic
for i in range(length_text):
    char = input_text[i]

    if char == "a":
        total += 1
    elif char == "e":
        total += 2
    elif char == "i":
        total += 3
    elif char == "o":
        total += 4
    elif char == "u":
        total += 5
# Print output
print(total)