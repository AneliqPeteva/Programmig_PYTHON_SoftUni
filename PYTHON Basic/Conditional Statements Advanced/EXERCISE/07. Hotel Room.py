# Read user input
mounts = input()
count_night = int(input())


# Logic
if mounts == "May" or mounts == "October":
    price_studio = 50
    price_apartment = 65
    total_sum_studio = count_night * price_studio
    total_sum_apartment = count_night * price_apartment
    if count_night > 14:
        total_sum_studio *= 0.70
    elif count_night > 7:
        total_sum_studio *= 0.95
elif mounts == "June" or mounts == "September":
    price_studio = 75.20
    price_apartment = 68.70
    total_sum_studio = count_night * price_studio
    total_sum_apartment = count_night * price_apartment
    if count_night > 14:
        total_sum_studio *= 0.80
elif mounts == "July" or mounts == "August":
    pass
    price_studio = 76
    price_apartment = 77
    total_sum_studio = count_night * price_studio
    total_sum_apartment = count_night * price_apartment

if count_night > 14:
    total_sum_apartment *= 0.90

# Print output
print(f"Apartment: {total_sum_apartment:.2f} lv.")
print(f"Studio: {total_sum_studio:.2f} lv.")