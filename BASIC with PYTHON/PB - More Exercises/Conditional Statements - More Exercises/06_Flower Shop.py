from math import ceil, floor
# Read user input
count_magnolias = int(input())
count_hyacinths = int(input())
count_roses = int(input())
count_cactus = int(input())
price_gift = float(input())

price_magnolias = 3.25
price_hyacinths = 4
price_roses = 3.50
price_cactus = 8
tax = 0.05

# Logic
sum_magnolias = count_magnolias * price_magnolias
sum_hyacinths = count_hyacinths * price_hyacinths
sum_roses = count_roses * price_roses
sum_cactus = count_cactus * price_cactus
sum = sum_magnolias + sum_hyacinths + sum_roses + sum_cactus
total_sum = sum - sum * tax

left_money = abs(total_sum - price_gift)

# Print output
if total_sum >= price_gift:
    print(f"She is left with {floor(left_money)} leva.")
else:
    print(f"She will have to borrow {ceil(left_money)} leva.")
