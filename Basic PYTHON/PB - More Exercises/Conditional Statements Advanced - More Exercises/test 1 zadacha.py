budget = float(input())
categories = input()
count_people = int(input())

vip_ticket = 499.99
normal_ticket = 249.99
price_transport = 0

if 1 <= count_people <= 4:
    price_transport = budget * 0.75
elif count_people <= 9:
    price_transport = budget * 0.60
elif count_people <= 24:
    price_transport = budget * 0.50
elif count_people <= 49:
    price_transport = budget * 0.40
elif count_people >= 50:
    price_transport = budget * 0.25


if categories == "VIP":
    total_sum = count_people * vip_ticket
elif categories == "Normal":
    total_sum = count_people * normal_ticket
razhodi = price_transport + total_sum
left_money = abs(budget - price_transport - total_sum)

if budget > razhodi:
    print(f"Yes! You have {left_money:.2f} leva left.")
else:
    print(f"Not enough money! You need {left_money:.2f} leva.")


