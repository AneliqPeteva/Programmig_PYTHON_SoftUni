list_of_phones = input().split(", ")
command = input()

while command != "End":
    command = command.split(" - ")
    command_type = command[0]
    phone = command[1]
    if command_type == "Add":
        if phone not in list_of_phones:
            list_of_phones.append(phone)
    elif command_type == "Remove":
        if phone in list_of_phones:
            list_of_phones.remove(phone)
    elif command_type == "Last":
        if phone in list_of_phones:
            phone_index = list_of_phones.index(phone)
            list_of_phones.append(list_of_phones.pop(phone_index))

    elif command_type == "Bonus phone":
        old_phone, new_phone = phone.split(":")
        if old_phone in list_of_phones:
            old_phone_index = list_of_phones.index(old_phone)
            list_of_phones.insert(old_phone_index + 1, new_phone)


    command = input()
print(*list_of_phones, sep=", ")