list_of_participants = input().split(", ")
participants = {}
while True:
    info_participants = input()
    if info_participants == "end of race":
        break
    name = ""
    distance = 0
    for element in info_participants:
        if element.isalpha():
            name += element
        elif element.isdigit():
            distance += int(element)
    if name in list_of_participants:
        if name not in participants.keys():
            participants[name] = distance
        else:
            participants[name] += distance

sort_participants =  sorted(participants.items(), key=lambda x: -x[1])

print(f"1st place: {sort_participants[0][0]}")
print(f"2nd place: {sort_participants[1][0]}")
print(f"3rd place: {sort_participants[2][0]}")

