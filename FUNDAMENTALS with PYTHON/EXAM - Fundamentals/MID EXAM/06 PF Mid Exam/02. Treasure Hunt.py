initial_loot = input().split("|")
command = input()
stolen_items = []
while command != "Yohoho!":
    command, *data = [x for x in command.split()]
    if "Loot" in command:
        for item in data:
            if item not in initial_loot:
                initial_loot.insert(0, item)

    elif "Drop" in command:
        index = int(data[0])
        if 0 <= index < len(initial_loot):
            initial_loot.append(initial_loot.pop(index))

    elif "Steal" in command:
        count = int(data[0])
        stolen_items = initial_loot[-count:]
        initial_loot = initial_loot[:-count]

        print(*stolen_items, sep=", ")
    command = input()

#if initial_loot:
#    average_treasure_gain = sum(len(x) for x in initial_loot) / len(initial_loot)
#    print(f"Average treasure gain: {average_treasure_gain:.2f} pirate credits.")
#else:
#    print("Failed treasure hunt.")
if len(initial_loot) == 0:
    print("Failed treasure hunt.")
else:
    sum_char = 0
    for current_word in initial_loot:
        sum_char += len(current_word)
    average_treasure_gain = sum_char / len(initial_loot)
    print(f"Average treasure gain: {average_treasure_gain:.2f} pirate credits.")




