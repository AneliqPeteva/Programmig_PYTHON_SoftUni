from collections import deque

quantity_food = int(input())
orders = deque([int(x) for x in input().split()])
max_quantity_order = max(orders)
print(max_quantity_order)

copy_order = orders.copy()

for current_order in orders:
    if quantity_food >= current_order:
        copy_order.popleft()
        quantity_food -= current_order
    else:
        print(f"Orders left: {' '.join([str(x) for x in copy_order])}")
        break

else:
    print("Orders complete")