budget_film =  float(input())
count_actor = int(input())
price_clothing_one_actor = float(input())

decor = budget_film * 0.1

if count_actor > 150:
    price_clothing_one_actor *= 0.9

total_sum = decor + count_actor * price_clothing_one_actor
left_money = abs(budget_film - total_sum)

if total_sum > budget_film:
    print("Not enough money!")
    print(f"Wingard needs {left_money:.2f} leva more.")
else:
    print("Action!")
    print(f"Wingard starts filming with {left_money:.2f} leva left.")

