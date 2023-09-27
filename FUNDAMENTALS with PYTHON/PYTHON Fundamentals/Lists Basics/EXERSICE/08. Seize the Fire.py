cells = input().split("#")
amount_of_water = int(input())
total_effort = 0
total_fire = 0
high = range(81, 125 + 1)
medium = range(51, 80 + 1)
low = range(1, 50 + 1)
fire_out_cells = []
for cell in cells:
    type_of_fire, value_of_ceil = cell.split(" = ")
    value_of_ceil = int(value_of_ceil)
    cell_is_valid = False
    if type_of_fire == "High":
        if value_of_ceil in high:
            cell_is_valid = True
    elif type_of_fire == "Medium":
        if value_of_ceil in medium:
            cell_is_valid = True
    elif type_of_fire == "Low":
        if value_of_ceil in low:
            cell_is_valid = True
    if cell_is_valid:
        if amount_of_water >= value_of_ceil:
            amount_of_water -= value_of_ceil
            fire_out_cells.append(value_of_ceil)
            total_fire += value_of_ceil
            total_effort += value_of_ceil * 0.25

print("Cells:")
for fire_out_cell in fire_out_cells:
    print(f"- {fire_out_cell}")
print(f"Effort: {total_effort:.2f}")
print(f"Total Fire: {total_fire}")
