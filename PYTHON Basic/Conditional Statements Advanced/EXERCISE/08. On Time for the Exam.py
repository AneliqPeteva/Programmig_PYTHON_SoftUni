# Read user input
exam_hour = int(input())
exam_min = int(input())
arrival_hour = int(input())
arrival_min = int(input())

exam_hour_to_min = exam_hour * 60
arrival_hour_to_min = arrival_hour * 60

all_exam_min = exam_hour_to_min + exam_min
all_arrival_min = arrival_hour_to_min + arrival_min

diff = abs(all_exam_min - all_arrival_min)
# Logic
if all_arrival_min > all_exam_min:
    print("Late")
    if diff < 60:
        print(f"{diff} minutes after the start")
    else:
        hours = diff // 60
        minutes = diff % 60
        if minutes < 10:
            print(f"{hours}:0{minutes} hours after the start")
        else:
            print(f"{hours}:{minutes} hours after the start")
elif all_arrival_min == all_exam_min or diff <= 30:
    print("On time")
    if 1 <= diff <= 30:
        print(f"{diff} minutes before the start")
else:
    print("Early")
    if diff < 60:
        print(f"{diff} minutes before the start")
    else:
        hours = diff // 60
        minutes = diff % 60
        if minutes < 10:
            print(f"{hours}:0{minutes} hours before the start")
        else:
            print(f"{hours}:{minutes} hours before the start")
# Print output