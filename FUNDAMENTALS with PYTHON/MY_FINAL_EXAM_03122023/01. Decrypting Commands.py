message = input()
command = input().split()

while command[0] != "Finish":
    if command[0] == "Replace":
        current_char = command[1]
        new_char = command[2]
        message = message.replace(current_char, new_char)
        print(message)
    elif command[0] == "Cut":
        start_index = int(command[1])
        end_index = int(command[2])
        if 0 <= start_index < len(message) and 0 <= end_index < len(message):
            message = message[:start_index] + message[end_index +1:]
            print(message)
        else:
            print("Invalid indices!")
    elif command[0] == "Make":
        if command[1] == "Upper":
            message = message.upper()
        elif command[1] == "Lower":
            message = message.lower()
        print(message)
    elif command[0] == "Check":
        string = command[1]
        if string in message:
            print(f"Message contains {string}")
        else:
            print(f"Message doesn't contain {string}")
    elif command[0] == "Sum":
        start_index = int(command[1])
        end_index = int(command[2])
        if 0 <= start_index < len(message) and 0 <= end_index < len(message):
            substring = message[start_index:end_index + 1]
            sum = 0
            for letter in substring:
                sum += ord(letter)
            print(sum)
        else:
            print("Invalid indices!")

    command = input().split()



