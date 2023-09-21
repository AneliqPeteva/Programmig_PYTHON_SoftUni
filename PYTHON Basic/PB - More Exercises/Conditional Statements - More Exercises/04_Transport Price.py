# Read user input
count_kilometers = int(input())
travel_day_or_night = input()

total_sum = 0

# Logic
if count_kilometers < 20:
    if travel_day_or_night == "day":
        total_sum = 0.70 + count_kilometers * 0.79
    else:
        total_sum = 0.70 + count_kilometers * 0.90
elif count_kilometers >= 100:
    total_sum = count_kilometers * 0.06
else:
    total_sum = count_kilometers * 0.09

# Print output
print(f"{total_sum:.2f}")

