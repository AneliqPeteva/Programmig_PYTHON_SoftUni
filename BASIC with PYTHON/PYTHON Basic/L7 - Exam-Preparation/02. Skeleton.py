min_control = int(input())
sec_control = int(input())
length_chute_meters = float(input())
sec_for_100_meters =  int(input())

#logic
all_sec_control = min_control * 60 + sec_control
total_reduced_time = (length_chute_meters / 120) * 2.5
time_marin = (length_chute_meters / 100) * sec_for_100_meters - total_reduced_time

diff = abs(time_marin - all_sec_control)
if time_marin > all_sec_control:
    print(f"No, Marin failed! He was {diff:.3f} second slower.")
else:
    print(f"Marin Bangiev won an Olympic quota!")
    print(f"His time is {time_marin:.3f}.")