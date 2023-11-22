def add_stop(ind, text):
    if 0 <= ind < len(text_travel) and 0 <= ind < len(text_travel):
        result = text_travel[:ind] + text + text_travel[ind:]
        return result
    return text_travel

def remove_stop(start_ind, end_ind):
    if 0 <= start_ind < len(text_travel) and 0 <= end_ind < len(text_travel):
        result = text_travel[:start_ind] + text_travel[end_ind + 1:]
        return result
    return text_travel

def switch(old, new):
    if old in text_travel:
        result = text_travel.replace(old, new)
        return result
    return text_travel

text_travel = input()

command = input().split(":")
while command[0] != "Travel":
    if command[0] == "Add Stop":
        index = int(command[1])
        string = command[2]
        text_travel = add_stop(index, string)
        print(text_travel)
    elif command[0] == "Remove Stop":
        start_index = int(command[1])
        end_index = int(command[2])
        text_travel = remove_stop(start_index, end_index)
        print(text_travel)
    elif command[0] == "Switch":
        old_string = command[1]
        new_string = command[2]
        text_travel = switch(old_string, new_string)
        print(text_travel)

    command = input().split(":")

print(f"Ready for world tour! Planned stops: {text_travel}")