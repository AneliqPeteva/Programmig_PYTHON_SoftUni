number = int(input())
info_plants = {}
for current_plants in range(number):
    plant, rarity = input().split("<->")
    if plant not in info_plants.keys():
        info_plants[plant] = []
    info_plants[plant] = [rarity, []]

command = input().split(": ")
while command[0] != "Exhibition":
    if command[0] == "Rate":
        plant, rating = command[1].split(" - ")
        if plant not in info_plants.keys():
            print("error")
        else:
            info_plants[plant][1].append(int(rating))
    elif command[0] == "Update":
        plant, new_rarity = command[1].split(" - ")
        if plant in info_plants.keys():
            info_plants[plant][0] = new_rarity
        else:
            print("error")
    elif command[0] == "Reset":
        plant = command[1]
        if plant in info_plants.keys():
            info_plants[plant][1].clear()
        else:
            print("error")
    command = input().split(": ")

print("Plants for the exhibition:")
for keys, values in info_plants.items():
    sum_rating_list = sum(values[1])
    len_rating_list = len(values[1])
    if sum_rating_list != 0 and len_rating_list != 0:
        average_rating = sum_rating_list / len_rating_list
        print(f"- {keys}; Rarity: {values[0]}; Rating: {average_rating:.2f}")
    else:
        print(f"- {keys}; Rarity: {values[0]}; Rating: {0:.2f}")