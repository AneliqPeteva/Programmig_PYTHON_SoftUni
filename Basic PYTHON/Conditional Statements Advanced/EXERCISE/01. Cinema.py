# Read user input
projection_type = input()
rows = int(input())
columns = int(input())

all_chair = rows * columns
total_sum = 0
# Logic
if projection_type == "Premiere":
    total_sum = all_chair * 12
elif projection_type == "Normal":
    total_sum = all_chair * 7.50
elif projection_type == "Discount":
    total_sum = all_chair * 5.0
# Print output
print(f"{total_sum:.2f} leva")