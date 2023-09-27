name_gifts = input().split(" ")
command = input()
while command != "No Money":
    command_type, *other_info = command.split()
    if "OutOfStock" in command_type:
        for index, name in enumerate(name_gifts):
            if other_info[-1] == name:
                name_gifts[index] = "None"
    elif "Required" in command_type:
        length = len(name_gifts)
        if length > int(other_info[-1]) >= 0:
            name_gifts[int(other_info[-1])] = other_info[0]
    elif "JustInCase" in command_type:
        name_gifts[-1] = other_info[-1]

    command = input()
print(" ".join(gift for gift in name_gifts if gift!= "None"))