health = 100

bitcoins = 0
rooms = input().split("|")
count_room = 0
for command in rooms:
    command_type, number = command.split()
    number = int(number)
    count_room += 1
    if command_type == "potion":
        if health + number > 100:
            number = 100 - health
        health += number
        print(f"You healed for {number} hp.")
        print(f"Current health: {health} hp.")

    elif command_type == "chest":
        bitcoins += number
        print(f"You found {number} bitcoins.")
    else:
        health -= number
        if health > 0:
            print(f"You slayed {command_type}.")
        else:
            print(f"You died! Killed by {command_type}." )
            print(f"Best room: {count_room}")
            break
else:
    print("You've made it!")
    print(f"Bitcoins: {bitcoins}")
    print(f"Health: {health}")


