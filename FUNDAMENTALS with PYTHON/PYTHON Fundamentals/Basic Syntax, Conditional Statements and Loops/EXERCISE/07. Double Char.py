''''
while True:
    command = input()
    new_word = ""
    if command == "End":
        break
    if command == "SoftUni":
        continue
    length_command = len(command)

    for i in range(length_command):
        char = command[i]
        new_word += char * 2
    print(new_word)

'''''

while True:
    command = input()
    new_word = ""
    if command == "End":
        break
    if command == "SoftUni":
        continue

    for character in command:
        new_word += character * 2
    print(new_word)