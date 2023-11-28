text = input()
command = input().split(">>>")

while command[0] != "Generate":

    if command[0] == "Contains":
        substring = command[1]
        if substring in text:
            print(f"{text} contains {substring}")
        else:
            print("Substring not found!")
    elif command[0] == "Flip":
        start_index = int(command[2])
        end_index = int(command[3])
        flip_string = text[start_index:end_index]
        if command[1] == "Upper":
            flip_string = flip_string.upper()
            text = text[:start_index] + flip_string + text[end_index:]
        elif command[1] == "Lower":
            flip_string = flip_string.lower()
            text = text[:start_index] + flip_string + text[end_index:]
        print(text)
    elif command[0] == "Slice":
        start_index = int(command[1])
        end_index = int(command[2])
        text = text[:start_index] + text[end_index:]
        print(text)
    command = input().split(">>>")
print(f"Your activation key is: {text}")