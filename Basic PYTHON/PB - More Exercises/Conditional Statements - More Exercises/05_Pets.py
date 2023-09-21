from math import ceil, floor

# Read user input
count_days = int(input())
left_food_kg = float(input())
food_dog_for_day_kg = float(input())
food_cat_for_day_kg = float(input())
food_turtle_for_day_grams = float(input())

# Logic
all_food_dog_kg = count_days * food_dog_for_day_kg
all_food_cat_kg = count_days * food_cat_for_day_kg
all_food_turtle_kg = (count_days * food_turtle_for_day_grams) / 1000
all_food = all_food_dog_kg + all_food_cat_kg + all_food_turtle_kg

remainder = abs(left_food_kg - all_food)

# Print output
if left_food_kg >= all_food:
    print(f"{floor(remainder)} kilos of food left.")
else:
    print(f"{ceil(remainder)} more kilos of food are needed.")

