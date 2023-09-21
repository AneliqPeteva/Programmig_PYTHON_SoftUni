from math import ceil
name_serial = input()
duration_epizode = int(input())
duration_break = int(input())

time_for_lunch = duration_break * 1/8
time_for_break = duration_break * 1/4
time_for_serial = duration_break - time_for_lunch - time_for_break

time_left = ceil(abs(time_for_serial - duration_epizode))

if time_for_serial >= duration_epizode:
    print(f"You have enough time to watch {name_serial} and left with {time_left:} minutes free time.")
else:
    print(f"You don't have enough time to watch {name_serial}, you need {time_left:} more minutes.")