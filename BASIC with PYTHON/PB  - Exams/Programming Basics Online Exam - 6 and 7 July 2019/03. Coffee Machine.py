#User input
drink = input()
sugar = input()
count_drink = int(input())
total_sum_drink = 0

#logic
if drink == "Espresso":
    if sugar == "Without":
        total_sum_drink = count_drink * 0.90
    elif sugar == "Normal":
        total_sum_drink = count_drink * 1.00
    elif sugar == "Extra":
        total_sum_drink = count_drink * 1.20
elif drink == "Cappuccino":
    if sugar == "Without":
        total_sum_drink = count_drink * 1.00
    elif sugar == "Normal":
        total_sum_drink = count_drink * 1.20
    elif sugar == "Extra":
        total_sum_drink = count_drink * 1.60
elif drink == "Tea":
    if sugar == "Without":
        total_sum_drink = count_drink * 0.50
    elif sugar == "Normal":
        total_sum_drink = count_drink * 0.60
    elif sugar == "Extra":
        total_sum_drink = count_drink * 0.70

if sugar == "Without":
    total_sum_drink *= 0.65
if drink == "Espresso" and count_drink >= 5:
    total_sum_drink *= 0.75
if total_sum_drink > 15:
    total_sum_drink *= 0.80

#print output
print(f"You bought {count_drink} cups of {drink} for {total_sum_drink:.2f} lv.")