zoo = {}

command = input().split(": ")
while command[0] != "EndDay":
    if command[0] == "Add":
        animal_name, needed_food_quantity, area = command[1].split("-")
        needed_food_quantity = int(needed_food_quantity)

        if animal_name not in zoo.keys():
            zoo[animal_name] = {"food_quantity": needed_food_quantity, "area": area}
        else:
            zoo[animal_name]["food_quantity"] += needed_food_quantity

    elif command[0] == "Feed":
        animal_name, food = command[1].split("-")
        food = int(food)
        if animal_name in zoo.keys():
            zoo[animal_name]["food_quantity"] -= food
            if zoo[animal_name]["food_quantity"] <= 0:
                print(f"{animal_name} was successfully fed")
                del zoo[animal_name]

    command = input().split(": ")
list_zoo = []
dict_area = {}
print("Animals:")
for animal_name, needed_food_quantity in zoo.items():
    print(f" {animal_name} -> {zoo[animal_name]['food_quantity']}g")
    list_zoo.append(zoo[animal_name]['area'])
print("Areas with hungry animals:")
for current_area in list_zoo:
    if current_area not in dict_area:
        dict_area[current_area] = 0
    dict_area[current_area] += 1
for area, number in dict_area.items():
    print(f"{area}: {number}")

