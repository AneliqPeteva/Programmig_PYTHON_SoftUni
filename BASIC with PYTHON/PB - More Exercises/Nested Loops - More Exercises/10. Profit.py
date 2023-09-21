count_1_lv = int(input())
count_2_lv = int(input())
count_5_lv = int(input())
sum = int(input())

for one_lv in range(count_1_lv + 1):
    for two_lv in range(count_2_lv + 1):
        for five_lv in range(count_5_lv + 1):
            if one_lv * 1 + two_lv * 2 + five_lv * 5 == sum:
                print(f"{one_lv} * 1 lv. + {two_lv} * 2 lv. + {five_lv} * 5 lv. = {sum} lv.")
