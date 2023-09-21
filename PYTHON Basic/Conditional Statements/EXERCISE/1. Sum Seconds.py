from math import floor

time_fyrst = int(input())
time_second = int(input())
time_third = int(input())

total_time = time_third + time_second + time_fyrst
minutes = total_time // 60
seconds = total_time % 60

minutes = floor(minutes)

if seconds < 10:
    print (f'{minutes}:0{seconds}')
else:
    print(f'{minutes}:{seconds}')
