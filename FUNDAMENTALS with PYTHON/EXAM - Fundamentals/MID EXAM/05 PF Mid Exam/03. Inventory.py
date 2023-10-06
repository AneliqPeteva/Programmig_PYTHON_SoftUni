journal = input().split(", ")

while True:
    command = input()
    if command == "Craft!":
        break
    if "Combine Items" in command:
        command_type = command.split(" - ")
        old_item, new_item = command_type[1].split(":")
        if old_item in journal:
            journal.insert(journal.index(old_item) + 1, new_item)
        continue

    command_type, item = command.split(" - ")
    if command_type == "Collect":
        if item not in journal:
            journal.append(item)
    elif command_type == "Drop":
        if item in journal:
            journal.remove(item)
    elif command_type == "Renew":
        if item in journal:
            journal.remove(item)
            journal.append(item)

print(*journal, sep=", ")


