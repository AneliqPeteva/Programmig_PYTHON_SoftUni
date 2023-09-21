tom_play_time_second = 30000
number_of_days_off = int(input())

time_game_work_day_second = 63
time_game_day_off_second = 127

work_days = 365 - number_of_days_off
all_time_for_game = work_days * time_game_work_day_second + number_of_days_off * time_game_day_off_second

time_left = abs(all_time_for_game - tom_play_time_second)
hours = time_left // 60
minutes = time_left % 60

if all_time_for_game > tom_play_time_second:
    print("Tom will run away")
    print(f"{hours} hours and {minutes} minutes more for play")
else:
    print("Tom sleeps well")
    print(f"{hours} hours and {minutes} minutes less for play")