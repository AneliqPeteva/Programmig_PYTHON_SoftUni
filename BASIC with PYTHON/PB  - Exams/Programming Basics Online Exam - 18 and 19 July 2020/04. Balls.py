from math import floor

number_balls = int(input())

counter_red = 0
counter_orange = 0
counter_yellow = 0
counter_white = 0
counter_black = 0
counter_other = 0
total_point = 0

for x in range(number_balls):
    current_color = input()
    if current_color == "red":
        counter_red += 1
        total_point += 5
    elif current_color == "orange":
        counter_orange += 1
        total_point += 10
    elif current_color == "yellow":
        counter_yellow += 1
        total_point += 15
    elif current_color == "white":
        counter_white += 1
        total_point += 20
    elif current_color == "black":
        counter_black += 1
        total_point = floor(total_point / 2)
    else:
        counter_other += 1
        total_point = total_point

print(f"Total points: {total_point}")
print(f"Red balls: {counter_red}")
print(f"Orange balls: {counter_orange}")
print(f"Yellow balls: {counter_yellow}")
print(f"White balls: {counter_white}")
print(f"Other colors picked: {counter_other}")
print(f"Divides from black balls: {counter_black}")