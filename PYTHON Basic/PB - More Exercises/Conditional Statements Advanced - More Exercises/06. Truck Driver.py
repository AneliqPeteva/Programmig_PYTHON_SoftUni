# Read user input
season = input()
kilometers_for_month = float(input())
total_sum = 0


# Logic
if kilometers_for_month <= 5000:
    if season == "Spring" or season == "Autumn":
        total_sum = (kilometers_for_month * 0.75) * 4
    elif season == "Summer":
        total_sum = (kilometers_for_month * 0.90) * 4
    elif season == "Winter":
        total_sum = (kilometers_for_month * 1.05) * 4
elif kilometers_for_month <= 10000:
    if season == "Spring" or season == "Autumn":
        total_sum = (kilometers_for_month * 0.95) * 4
    elif season == "Summer":
        total_sum = (kilometers_for_month * 1.10) * 4
    elif season == "Winter":
        total_sum = (kilometers_for_month * 1.25) * 4
elif kilometers_for_month <= 20000:
    total_sum = (kilometers_for_month * 1.45) * 4

total_sum *= 0.90

# Print output
print(f"{total_sum:.2f}")