from collections import deque

food_portions = [int(x) for x in input().split(", ")]
stamina = deque([int(x) for x in input().split(", ")])

conquered_peaks = []
peaks_data = deque([
    ('Vihren', 80),
    ('Kutelo', 90),
    ('Banski Suhodol', 100),
    ('Polezhan', 60),
    ('Kamenitza', 70),
])
days = 7
for current_day in range(days):
    current_food_portion = food_portions.pop()
    current_stamina = stamina.popleft()

    sum_food_stamina = current_food_portion + current_stamina



    if sum_food_stamina >= peaks_data[0][1]:
        current_mountain_peak, difficulty_level = peaks_data.popleft()
        conquered_peaks.append(current_mountain_peak)
        if len(conquered_peaks) == 5:
            print("Alex did it! He climbed all top five Pirin peaks in one week -> @FIVEinAWEEK\nConquered peaks:")
            print("\n".join(conquered_peaks))
            exit()
print("Alex failed! He has to organize his journey better next time -> @PIRINWINS")
if conquered_peaks:
    print("Conquered peaks:")
    print("\n".join(conquered_peaks))




