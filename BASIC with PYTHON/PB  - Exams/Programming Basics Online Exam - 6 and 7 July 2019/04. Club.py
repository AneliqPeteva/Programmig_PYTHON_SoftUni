#User input
profit = float(input())
total_sum = 0
all_sum = 0

#logic
while True:
    name_cocktail = input()
    if name_cocktail == "Party!":
        print(f"We need {profit - all_sum:.2f} leva more.")
        break
    count_cocktails = int(input())
    price_cocktail = len(name_cocktail)
    total_sum = price_cocktail * count_cocktails
    if total_sum % 2 != 0:
        total_sum *= 0.75
    all_sum += total_sum
    if all_sum >= profit:
        print("Target acquired.")
        break

print(f"Club income - {all_sum:.2f} leva.")