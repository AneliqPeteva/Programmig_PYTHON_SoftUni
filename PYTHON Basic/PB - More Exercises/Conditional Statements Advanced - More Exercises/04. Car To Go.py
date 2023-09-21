# Read user input
budget = float(input())
season = input()
class_car = ""
price_car = 0
# Logic
if budget <= 100:
    class_car = "Economy class"
    if season == "Summer":
        type_car = "Cabrio"
        price_car = budget * 0.35
    elif season == "Winter":
        type_car = "Jeep"
        price_car = budget * 0.65
elif budget <= 500:
    class_car = "Compact class"
    if season == "Summer":
        type_car = "Cabrio"
        price_car = budget * 0.45
    elif season == "Winter":
        type_car = "Jeep"
        price_car = budget * 0.80
elif budget > 500:
    class_car = "Luxury class"
    if season == "Summer" or season == "Winter":
        type_car = "Jeep"
        price_car = budget * 0.90

# Print output
print(f"{class_car}")
print(f"{type_car} - {price_car:.2f}")