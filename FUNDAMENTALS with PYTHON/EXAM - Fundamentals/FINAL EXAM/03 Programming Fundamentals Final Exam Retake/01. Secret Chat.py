text_message = input()

command_text = input().split(":|:")

while command_text[0] != "Reveal":
    command = command_text[0]
    if command == "InsertSpace":
        index = int(command_text[1])
        text_message = text_message[:index] + " " + text_message[index:]
        print(text_message)
    elif command == "Reverse":
        substring = command_text[1]
        if substring in text_message:
            substring_reverse = substring[::-1]
            text_message = text_message.replace(substring, substring_reverse, 1)
            print(text_message)
        else:
            print("error")
    elif command == "ChangeAll":
        substring = command_text[1]
        replacement = command_text[2]
        if substring in text_message:
            text_message = text_message.replace(substring, replacement)
        print(text_message)
    command_text = input().split(":|:")


print(f"You have a new text message: {text_message}")