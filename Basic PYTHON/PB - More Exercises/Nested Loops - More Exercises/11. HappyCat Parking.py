count_day = int(input())
count_hours = int(input())

all_total_sum = 0
current_day = 1

price = 0
for day in range(1, count_day + 1):
    sum_for_day = 0
    for hours in range(1, count_hours + 1):
        if day % 2 == 0 and hours % 2 != 0:
            price = 2.50
        elif day % 2 != 0 and hours % 2 == 0:
            price = 1.25
        else:
            price = 1
        sum_for_day += price
    all_total_sum += sum_for_day
    print(f"Day: {current_day} - {sum_for_day:.2f} leva")
    current_day += 1
print(f"Total: {all_total_sum:.2f} leva")
