health = 100
bitcoins = 0
room = input().split("|")
current_health = health
count_room = 0
is_go_through = False
for current_room in room:
    command, digit = current_room.split()
    count_room += 1
    digit = int(digit)
    if command == "potion":
        if current_health + digit <= health:
            current_health += digit
            print(f"You healed for {digit} hp.")
            print(f"Current health: {current_health} hp.")
        else:
            amount = health - current_health
            current_health += amount
            print(f"You healed for {amount} hp.")
            print(f"Current health: {current_health} hp.")
    elif command == "chest":
        print(f"You found {digit} bitcoins.")
        bitcoins += digit
    else:
        current_health -= digit
        if current_health > 0:
            print(f"You slayed {command}.")
        else:
            print(f"You died! Killed by {command}.")
            print(f"Best room: {count_room}")
            is_go_through = True
            break

if is_go_through == False:
    print("You've made it!")
    print(f"Bitcoins: {bitcoins}")
    print(f"Health: {current_health}")



