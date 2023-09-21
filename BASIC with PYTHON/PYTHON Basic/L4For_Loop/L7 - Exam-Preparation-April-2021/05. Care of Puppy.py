count_food_kg = int(input())
foot_for_one_eat_gram = input()
all_qty_food = 0
count_food_gram = count_food_kg * 1000

while foot_for_one_eat_gram != "Adopted":
    foot_for_one_eat_gram = int(foot_for_one_eat_gram)
    all_qty_food += foot_for_one_eat_gram
    foot_for_one_eat_gram = input()

if all_qty_food <= count_food_gram:
    print(f"Food is enough! Leftovers: {count_food_gram - all_qty_food} grams." )
else:
    print(f"Food is not enough. You need {all_qty_food - count_food_gram} grams more." )