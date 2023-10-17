status_pirates_ship = [int(num) for num in input().split(">")]
status_warship = [int(num) for num in input().split(">")]
maximum_health = int(input())


is_has_stalemate_occurs = True
while is_has_stalemate_occurs:
    count_needed_section_repair = 0
    input_lines = input().split()
    if input_lines[0] == "Retire":
        break
#    input_lines = input_lines.split()
    if input_lines[0] == "Fire":
        index = int(input_lines[1])
        damage = int(input_lines[2])
        if 0 <= index < len(status_warship):
            status_warship[index] -= damage
            if status_warship[index] <= 0:
                print("You won! The enemy ship has sunken.")
                is_has_stalemate_occurs = False
                break
    elif input_lines[0] == "Defend":
        start_index = int(input_lines[1])
        end_index = int(input_lines[2])
        damage = int(input_lines[3])
        if 0 <= start_index < len(status_pirates_ship) and 0 <= end_index < len(status_pirates_ship):
            for current_index in range(start_index, end_index + 1):
                status_pirates_ship[current_index] -= damage
                if status_pirates_ship[current_index] <= 0:
                    print("You lost! The pirate ship has sunken.")
                    is_has_stalemate_occurs = False
                    break

    elif input_lines[0] == "Repair":
        index = int(input_lines[1])
        health = int(input_lines[2])
        if 0 <= index < len(status_pirates_ship):
            status_pirates_ship[index] = min(maximum_health, status_pirates_ship[index] + health)
    elif input_lines[0] == "Status":
        section_needed_repair = maximum_health * 0.20
        for current_section in status_pirates_ship:
            if current_section < section_needed_repair:
                count_needed_section_repair += 1
        print(f"{count_needed_section_repair} sections need repair.")

if is_has_stalemate_occurs:
    print(f"Pirate ship status: {sum(status_pirates_ship)}")
    print(f"Warship status: {sum(status_warship)}")