number_windows = int(input())
type_windows = input()
way_delivery = input()
price_per_windows = 0

if type_windows == "90X130":
    price_per_windows = 110
    if 30 < number_windows <= 60:
        price_per_windows *= 0.95
    elif number_windows > 60:
        price_per_windows *= 0.92
elif type_windows == "100X150":
    price_per_windows = 140
    if 40 < number_windows <= 80:
        price_per_windows *= 0.94
    elif number_windows > 80:
        price_per_windows *= 0.90
elif type_windows == "130X180":
    price_per_windows = 190
    if 20 < number_windows <= 50:
        price_per_windows *= 0.93
    elif number_windows > 50:
        price_per_windows *= 0.88
elif type_windows == "200X300":
    price_per_windows = 250
    if 25 < number_windows <= 50:
        price_per_windows *= 0.91
    elif number_windows > 50:
        price_per_windows *= 0.86

total = number_windows * price_per_windows
if way_delivery == "With delivery":
    total += 60
if number_windows > 99:
    total *= 0.96

if number_windows < 10:
    print("Invalid order")
else:
    print(f"{total:.2f} BGN")