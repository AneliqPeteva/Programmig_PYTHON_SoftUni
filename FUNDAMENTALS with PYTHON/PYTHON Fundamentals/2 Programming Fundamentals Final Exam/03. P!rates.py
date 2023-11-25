cities = {}
# Collecting cities information
command = input().split("||")
while command[0] != "Sail":
    city, population, gold = command[0], int(command[1]), int(command[2])
    if city not in cities.keys():
        cities[city] = {"population": 0, "gold": 0}
        # {"Tortuga": {"population": 0, "gold": 0}}
    cities[city]["population"] += population
    cities[city]["gold"] += gold
    command = input().split("||")
# Doing events
command = input().split("=>")
while command[0] != "End":
    action = command[0]
    if action == "Plunder":
        town, people, gold = command[1], int(command[2]), int(command[3])
        print(f"{town} plundered! {gold} gold stolen, {people} citizens killed.")
        cities[town]["population"] -= people
        cities[town]["gold"] -= gold
        if cities[town]["population"] == 0 or cities[town]["gold"] == 0:
            cities.pop(town)
            print(f"{town} has been wiped off the map!")
    elif action == "Prosper":
        town, gold = command[1], int(command[2])
        if gold < 0:
            print("Gold added cannot be a negative number!")
        else:
            cities[town]["gold"] += gold
            print(f"{gold} gold added to the city treasury. {town} now has {cities[town]['gold']} gold.")
    command = input().split("=>")
if cities:
    print(f"Ahoy, Captain! There are {len(cities)} wealthy settlements to go to:")
    for town, town_information in cities.items():
        print(f'{town} -> Population: {town_information["population"]} citizens, Gold: {town_information["gold"]} kg')
else:
    print("Ahoy, Captain! All targets have been plundered and destroyed!")



# command = input().split("||")
# info_town = {}
# while command[0] != "Sail":
#     name = command[0]
#     population = int(command[1])
#     gold = int(command[2])
#
#     if name not in info_town.keys():
#         info_town[name] = [population, gold]
#     else:
#         info_town[name][0] += population
#         info_town[name][1] += gold
#
#     command = input().split("||")
#
# events = input().split("=>")
# while events[0] != "End":
#     command = events[0]
#     name = events[1]
#     if command == "Plunder":
#         people = int(events[2])
#         gold = int(events[3])
#         print(f"{name} plundered! {gold} gold stolen, {people} citizens killed.")
#         info_town[name][0] -= people
#         info_town[name][1] -= gold
#         if info_town[name][0] == 0 or info_town[name][1] == 0:
#             print(f"{name} has been wiped off the map!")
#             info_town.pop(name)
#     elif command == "Prosper":
#         gold = int(events[2])
#         if gold > 0:
#             info_town[name][1] += gold
#             total_gold = info_town[name][1]
#             print(f"{gold} gold added to the city treasury. {name} now has {total_gold} gold.")
#         else:
#             print(f"Gold added cannot be a negative number!")
#
#     events = input().split("=>")
#
# count_town = len(info_town)
# if count_town > 0:
#     print(f"Ahoy, Captain! There are {count_town} wealthy settlements to go to:")
#     for current_town, info in info_town.items():
#         print(f"{current_town} -> Population: {info[0]} citizens, Gold: {info[1]} kg")
# else:
#     print("Ahoy, Captain! All targets have been plundered and destroyed!")