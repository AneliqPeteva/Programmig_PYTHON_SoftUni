decrypted_message = input()

operation = input()

while operation != "Decode":
    operation = operation.split("|")
    if operation[0] == "Move":
        number_of_letters = int(operation[1])
        decrypted_message = decrypted_message[number_of_letters:] + decrypted_message[:number_of_letters]
    elif operation[0] == "Insert":
        index = int(operation[1])
        value = operation[2]
        decrypted_message = decrypted_message[:index] + value + decrypted_message[index:]
    elif operation[0] == "ChangeAll":
        substring = operation[1]
        replacement = operation[2]
        decrypted_message = decrypted_message.replace(substring, replacement)
    operation = input()

print(f"The decrypted message is: {decrypted_message}")