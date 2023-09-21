# Read user input
budget = float(input())
season = input()
place = ""
location = ""
total_sum = 0

# Logic
if budget <= 1000:
    place = "Camp"
    if season == "Summer":
        location = "Alaska"
        total_sum = budget * 0.65
    elif season == "Winter":
        location = "Morocco"
        total_sum = budget * 0.45
elif budget <= 3000:
    place = "Hut"
    if season == "Summer":
        location = "Alaska"
        total_sum = budget * 0.80
    elif season == "Winter":
        location = "Morocco"
        total_sum = budget * 0.60
elif budget > 3000:
    place = "Hotel"
    if season == "Summer":
        location = "Alaska"
        total_sum = budget * 0.90
    elif season == "Winter":
        location = "Morocco"
        total_sum = budget * 0.90


# Print output
print(f"{location} - {place} - {total_sum:.2f}")