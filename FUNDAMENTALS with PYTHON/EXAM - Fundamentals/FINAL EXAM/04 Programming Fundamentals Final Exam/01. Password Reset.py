password = input()
command = input().split()

while command[0] != "Done":
    if command[0] == "TakeOdd":
        text = ""
        for index in range(len(password)):
            if index % 2 != 0:
                text += password[index]
        password = text
        print(password)
    elif command[0] == "Cut":
        index = int(command[1])
        length = int(command[2])
        password = password[:index] + password[index + length:]
        print(password)
    elif command[0] == "Substitute":
        substring = command[1]
        substitute = command[2]
        if substring in password:
            password = password.replace(substring, substitute)
            print(password)
        else:
            print("Nothing to replace!")

    command = input().split()

print(f"Your password is: {password}")