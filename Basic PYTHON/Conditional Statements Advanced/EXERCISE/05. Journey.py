# Read user input
budget = float(input())
season = input()
destination = ""
total_sum = 0
place_vacantion = ""
# Logic
if budget <= 100:
    destination = "Bulgaria"
    if season == "summer":
        place_vacantion = "Camp"
        total_sum = budget * 0.70
    elif season == "winter":
        place_vacantion = "Hotel"
        total_sum = budget * 0.30
elif budget > 1000:
    destination = "Europe"
    place_vacantion = "Hotel"
    total_sum = budget * 0.10
else:
    destination = "Balkans"
    if season == "summer":
        place_vacantion = "Camp"
        total_sum = budget * 0.60
    elif season == "winter":
        place_vacantion = "Hotel"
        total_sum = budget * 0.20
left_money = budget - total_sum
# Print output

print(f"Somewhere in {destination}")
print(f"{place_vacantion} - {left_money:.2f}")