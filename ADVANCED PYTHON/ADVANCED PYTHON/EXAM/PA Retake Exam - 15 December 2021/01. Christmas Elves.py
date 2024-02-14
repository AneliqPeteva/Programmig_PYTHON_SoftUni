from collections import deque

energy_elf = deque([int(x) for x in input().split()])
number_materials = [int(x) for x in input().split()]

total_number_of_toys = 0
total_used_energy = 0
count_elf = 0

while energy_elf and number_materials:

    current_energy_elf = energy_elf.popleft()
    if current_energy_elf < 5:
        continue
    current_materials = number_materials.pop()
    count_elf += 1
    if count_elf % 5 == 0:
        if count_elf % 3 == 0:
            total_number_of_toys -= 2
        elif current_energy_elf >= current_materials:
            total_used_energy += current_materials
        else:
            current_energy_elf *= 2
            energy_elf.append(current_energy_elf)
            current_materials = int(current_materials / 2)
            number_materials.append(current_materials)

    elif count_elf % 3 == 0:
        current_materials = current_materials * 2
        if current_energy_elf >= current_materials:
            total_number_of_toys += 2
            total_used_energy += current_materials
            current_energy_elf = current_energy_elf - current_materials + 1
            energy_elf.append(current_energy_elf)
        else:
            current_energy_elf *= 2
            energy_elf.append(current_energy_elf)
            current_materials = int(current_materials / 2)
            number_materials.append(current_materials)


    else:
        if current_energy_elf >= current_materials:
            total_number_of_toys += 1
            total_used_energy += current_materials
            current_energy_elf = current_energy_elf - current_materials + 1
            energy_elf.append(current_energy_elf)
        else:
            current_energy_elf *= 2
            energy_elf.append(current_energy_elf)
            current_materials = int(current_materials / 2)
            number_materials.append(current_materials)



print(f"Toys: {total_number_of_toys}")
print(f"Energy: {total_used_energy}")
if energy_elf:
    print(f"Elves left: {', '.join(str(x) for x in energy_elf)}")
if number_materials:
    print(f"Boxes left: {', '.join(str(x) for x in number_materials)}")




