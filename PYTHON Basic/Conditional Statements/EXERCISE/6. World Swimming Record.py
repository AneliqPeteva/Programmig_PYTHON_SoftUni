from math import floor

record_seconds = float(input())
distance_meters = float(input())
time_seconds_swims_one_meters = float(input())

total_distance_second = distance_meters * time_seconds_swims_one_meters
additional_second = floor(distance_meters / 15) * 12.5

total_time_second = total_distance_second + additional_second

if total_time_second < record_seconds:
    print(f"Yes, he succeeded! The new world record is {total_time_second:.2f} seconds.")
else:
    print(f"No, he failed! He was {(total_time_second - record_seconds):.2f} seconds slower.")
