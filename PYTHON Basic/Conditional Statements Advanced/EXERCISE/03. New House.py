# Read user input
type_flowers = input()
count_flowers = int(input())
budget = int(input())

price_rose = 5
price_dahlia = 3.80
price_tulip = 2.8
price_narcissus = 3
price_gladiola = 2.5

sum_roses = count_flowers * price_rose
sum_dahlia = count_flowers * price_dahlia
sum_tulip = count_flowers * price_tulip
sum_narcissus = count_flowers * price_narcissus
sum_gladiola = count_flowers * price_gladiola
total_sum = 0
# Logic
if type_flowers == "Roses":
    if count_flowers > 80:
        total_sum = sum_roses * 0.90
    else:
        total_sum = sum_roses
elif type_flowers == "Dahlias":
    if count_flowers > 90:
        total_sum = sum_dahlia * 0.85
    else:
        total_sum = sum_dahlia
elif type_flowers == "Tulips":
    if count_flowers > 80:
        total_sum = sum_tulip * 0.85
    else:
        total_sum = sum_tulip
elif type_flowers == "Narcissus":
    if count_flowers < 120:
        total_sum = sum_narcissus * 1.15
    else:
        total_sum = sum_narcissus
elif type_flowers == "Gladiolus":
    if count_flowers < 80:
        total_sum = sum_gladiola * 1.20
    else:
        total_sum = sum_gladiola

left_money = abs(budget - total_sum)

# Print output
if total_sum <= budget:
    print(f"Hey, you have a great garden with {count_flowers} {type_flowers} and {left_money:.2f} leva left.")
else:
    print(f"Not enough money, you need {left_money:.2f} leva more.")
