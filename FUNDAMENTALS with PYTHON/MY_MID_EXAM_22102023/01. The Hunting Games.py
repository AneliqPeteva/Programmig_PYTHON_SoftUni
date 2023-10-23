days_of_the_adventure = int(input())
players_number = int(input())
energy_group = float(input())
water_per_day_for_one_person = float(input())
food_per_day_for_one_person = float(input())

current_food = (days_of_the_adventure * food_per_day_for_one_person) * players_number
current_water = (days_of_the_adventure * water_per_day_for_one_person) * players_number

for current_day in range(1, days_of_the_adventure + 1):

    quantity_energy_lost = float(input())
    energy_group -= quantity_energy_lost
    if energy_group <= 0:
        break

    if current_day % 2 == 0:
        energy_group += energy_group * 0.05
        current_water *= 0.70

    if current_day % 3 == 0:
        current_food -= current_food / players_number
        energy_group += energy_group * 0.10



if energy_group <= 0:
    print(f"You will run out of energy. You will be left with {current_food:.2f} food and {current_water:.2f} water.")
else:
    print(f"You are ready for the quest. You will be left with - {energy_group:.2f} energy!")