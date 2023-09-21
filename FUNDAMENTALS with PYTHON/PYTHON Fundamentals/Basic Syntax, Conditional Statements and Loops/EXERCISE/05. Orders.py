number_of_orders = int(input())
price_for_coffee = 0
total_price = 0

for i in range(number_of_orders):
    price_per_capsule = float(input())
    days = int(input())
    capsules_needed_per_day = int(input())

    if 1 <= days <= 31 and 1 <= capsules_needed_per_day <= 2000 and 0.01 <= price_per_capsule <= 100:
        price_for_coffee = (capsules_needed_per_day * price_per_capsule) * days
        print(f"The price for the coffee is: ${price_for_coffee:.2f}")
        total_price += price_for_coffee
    else:
        continue

print(f"Total: ${total_price:.2f}")
