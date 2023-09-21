# Read user input
budget = int(input())
season = input()
count_fisherman = int(input())
rent_boat = 0

# Logic
if season == "Spring":
    rent_boat = 3000
elif season == "Summer" or season == "Autumn":
    rent_boat = 4200
elif season == "Winter":
    rent_boat = 2600

if count_fisherman <= 6:
    rent_boat *= 0.90
elif count_fisherman >= 12:
    rent_boat *= 0.75
else:
    rent_boat *= 0.85

if count_fisherman % 2 == 0 and season != "Autumn":
    rent_boat *= 0.95
else:
    rent_boat = rent_boat

left_money = abs(budget - rent_boat)

# Print output
if rent_boat <= budget:
    print(f"Yes! You have {left_money:.2f} leva left.")
else:
    print(f"Not enough money! You need {left_money:.2f} leva.")