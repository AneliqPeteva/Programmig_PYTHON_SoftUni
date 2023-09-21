size_eggs = input()
color_eggs = input()
count_lots = int(input())
sum_for_eggs = 0

#logic
if size_eggs == "Large":
    if color_eggs == "Red":
        price = 16
        sum_for_eggs = price * count_lots
    elif color_eggs == "Green":
        price = 12
        sum_for_eggs = price * count_lots
    elif color_eggs == "Yellow":
        price = 9
        sum_for_eggs = price * count_lots
elif size_eggs == "Medium":
    if color_eggs == "Red":
        price = 13
        sum_for_eggs = price * count_lots
    elif color_eggs == "Green":
        price = 9
        sum_for_eggs = price * count_lots
    elif color_eggs == "Yellow":
        price = 7
        sum_for_eggs = price * count_lots
elif size_eggs == "Small":
    if color_eggs == "Red":
        price = 9
        sum_for_eggs = price * count_lots
    elif color_eggs == "Green":
        price = 8
        sum_for_eggs = price * count_lots
    elif color_eggs == "Yellow":
        price = 5
        sum_for_eggs = price * count_lots

total_sum = sum_for_eggs - (sum_for_eggs * 0.35)

#print
print(f"{total_sum:.2f} leva.")

