def move(number):
    result = decrypted_message[number:] + decrypted_message[:number]
    return result

def insert(num_index, val):
    result = decrypted_message[:num_index] + val + decrypted_message[num_index:]
    return result

def change_all(substr, replace):
    result = decrypted_message.replace(substr, replace)
    return result

decrypted_message = input()
command = input().split("|")

while command[0] != "Decode":
    if command[0] == "Move":
        number_of_letters = int(command[1])
        decrypted_message = move(number_of_letters)
    elif command[0] == "Insert":
        index = int(command[1])
        value = command[2]
        decrypted_message = insert(index, value)
    elif command[0] == "ChangeAll":
        substring = command[1]
        replacement = command[2]
        decrypted_message = change_all(substring, replacement)

    command = input().split("|")

print(f"The decrypted message is: {decrypted_message}")



