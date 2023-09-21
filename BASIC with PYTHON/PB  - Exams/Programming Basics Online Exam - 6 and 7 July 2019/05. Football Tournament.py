#User input
name_football_team = input()
number_of_matches_played = int(input())
count_w = 0
count_d = 0
count_l = 0
total_points = 0

#logic

for i in range(number_of_matches_played):
    result = input()
    if result == "W":
        total_points += 3
        count_w += 1
    elif result == "D":
       total_points += 1
       count_d += 1
    elif result == "L":
        total_points = total_points
        count_l += 1


#print output
if number_of_matches_played == 0:
    print(f"{name_football_team} hasn't played any games during this season.")
elif number_of_matches_played >= 1:
    percent = count_w / number_of_matches_played * 100
    print(f"{name_football_team} has won {total_points} points during this season.")
    print("Total stats:")
    print(f"## W: {count_w}")
    print(f"## D: {count_d}")
    print(f"## L: {count_l}")
    print(f"Win rate: {percent:.2f}%")
