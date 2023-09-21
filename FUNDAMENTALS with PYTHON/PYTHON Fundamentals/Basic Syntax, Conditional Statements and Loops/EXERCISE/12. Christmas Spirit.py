quantity_of_decorations = int(input())
days_left = int(input())
budget = 0
total_spirit = 0
price_ornament_set = 2
price_tree_skirt = 5
price_tree_garland = 3
price_lights = 15
points_ornament_set = 5
points_tree_skirt = 3
points_tree_garland = 10
points_lights = 17

for current_day in range(1, days_left + 1):
    if current_day % 11 == 0:
        quantity_of_decorations += 2
    if current_day % 2 == 0:
        budget += quantity_of_decorations * price_ornament_set
        total_spirit += points_ornament_set
    if current_day % 3 == 0:
        budget += quantity_of_decorations * (price_tree_skirt + price_tree_garland)
        total_spirit += points_tree_skirt + points_tree_garland
    if current_day % 5 == 0:
        budget += quantity_of_decorations * price_lights
        total_spirit += points_lights
        if current_day % 3 == 0:
            total_spirit += 30
    if current_day % 10 == 0:
        total_spirit -= 20
        budget += price_tree_skirt + price_tree_garland + price_lights
if days_left % 10 == 0:
    total_spirit -= 30

print(f"Total cost: {budget}")
print(f"Total spirit: {total_spirit}")

