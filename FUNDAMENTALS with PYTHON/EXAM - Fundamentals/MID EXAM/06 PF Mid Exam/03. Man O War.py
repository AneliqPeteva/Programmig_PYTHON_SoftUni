status_pirate_ship = [int(x) for x in input().split(">")]
status_of_the_warship = [int(x) for x in input().split(">")]
maximum_health = int(input())


while True:
    user_input = input()
    count_section = 0
    if user_input == "Retire":
        break

    command = user_input.split()
    if "Fire" in command:
        index = int(command[1])
        damage = int(command[2])
        if 0 <= index < len(status_of_the_warship):
            status_of_the_warship[index] -= damage
            if status_of_the_warship[index] <= 0:
                print("You won! The enemy ship has sunken.")
                exit()
    elif "Defend" in command:
        start_index = int(command[1])
        end_index = int(command[2])
        damage = int(command[3])
        if 0 <= start_index < len(status_pirate_ship) and 0 <= end_index < len(status_pirate_ship):
            for current_index in range(start_index, end_index + 1):
                status_pirate_ship[current_index] -= damage
                if status_pirate_ship[current_index] <= 0:
                    print("You lost! The pirate ship has sunken.")
                    exit()
    elif "Repair" in command:
        index = int(command[1])
        health = int(command[2])
        if 0 <= index < len(status_pirate_ship):
            status_pirate_ship[index] += health
            if status_pirate_ship[index] >= maximum_health:
                status_pirate_ship[index] = maximum_health
    elif "Status" in command:
        sections_need_repair = maximum_health * 0.20
        for current_section in status_pirate_ship:
            if current_section < sections_need_repair:
                count_section += 1
        print(f"{count_section} sections need repair.")

print(f"Pirate ship status: {sum(status_pirate_ship)}")
print(f"Warship status: {sum(status_of_the_warship)}")


