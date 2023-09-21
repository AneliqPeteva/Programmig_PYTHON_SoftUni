#User input
budget = float(input())
count_nights = int(input())
price_night = float(input())
percent_other_expenses = int(input())
all_price_nights = 0
#logic

if count_nights > 7:
    price_night *= 0.95
    all_price_nights = count_nights * price_night
else:
    all_price_nights = count_nights * price_night

sum_other_expenses = budget * (percent_other_expenses / 100)
total_sum = all_price_nights + sum_other_expenses

#print output
diff = abs(total_sum - budget)
if total_sum <= budget:
    print(f"Ivanovi will be left with {diff:.2f} leva after vacation.")
else:
    print(f"{diff:.2f} leva needed.")