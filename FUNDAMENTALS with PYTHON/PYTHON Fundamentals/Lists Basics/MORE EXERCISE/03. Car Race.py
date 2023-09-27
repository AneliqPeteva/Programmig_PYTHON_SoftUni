number = input().split()
sum_left_part = 0
sum_right_part = 0
middle_number = len(number) // 2
left_part = number[0:middle_number]
right_part = number[middle_number+1:][::-1]
for num in left_part:
    num = int(num)
    if num == 0:
        sum_left_part *= 0.8
    sum_left_part += num
for num in right_part:
    num = int(num)
    if num == 0:
        sum_right_part *= 0.8
    sum_right_part += num

if sum_left_part < sum_right_part:
    print(f"The winner is left with total time: {sum_left_part:.1f}")
else:
    print(f"The winner is right with total time: {sum_right_part:.1f}")