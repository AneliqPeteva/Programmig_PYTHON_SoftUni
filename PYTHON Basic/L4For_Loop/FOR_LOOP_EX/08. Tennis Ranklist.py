from math import floor
# Read user input
count_tournaments = int(input())
start_point = int(input())
count_w = 0
total_point = 0

# Logic
for i in range(count_tournaments):
    stage_tournaments = input()
    if stage_tournaments == "W":
        total_point += 2000
        count_w +=1
    elif stage_tournaments == "F":
        total_point += 1200
    elif stage_tournaments == "SF":
        total_point += 720

total_all_points = start_point + total_point
avarage_point = floor(total_point / count_tournaments)
percent = (count_w / count_tournaments) * 100
# Print output
print(f"Final points: {total_all_points}")
print(f"Average points: {avarage_point}")
print(f"{percent:.2f}%")