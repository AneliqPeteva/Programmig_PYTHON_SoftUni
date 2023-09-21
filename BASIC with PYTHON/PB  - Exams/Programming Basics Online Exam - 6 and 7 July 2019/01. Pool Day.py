from math import ceil
#User input
count_people = int(input())
entrance_fee = float(input())
price_for_one_sunbed = float(input())
price_for_one_umbrella = float(input())

#logic
total_sum_entrance = count_people * entrance_fee
total_sum_umbrella = (ceil(count_people / 2)) * price_for_one_umbrella
total_sum_sunbed = (ceil(count_people * 0.75)) * price_for_one_sunbed
all_total_sum = total_sum_sunbed + total_sum_umbrella + total_sum_entrance

#print output
print(f"{all_total_sum:.2f} lv.")