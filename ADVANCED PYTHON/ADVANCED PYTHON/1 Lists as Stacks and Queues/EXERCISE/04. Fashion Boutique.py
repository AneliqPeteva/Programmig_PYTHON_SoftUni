clothes_stack = [int(x) for x in input().split()]
capacity_rack = int(input())
number_rack = 1

current_capacity_rack = capacity_rack

while clothes_stack:
    current_cloth = clothes_stack.pop()
    if current_capacity_rack >= current_cloth:
        current_capacity_rack -= current_cloth
    else:
        number_rack += 1
        current_capacity_rack = capacity_rack - current_cloth

print(number_rack)