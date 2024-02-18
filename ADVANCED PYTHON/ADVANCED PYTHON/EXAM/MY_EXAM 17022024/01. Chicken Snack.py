from collections import deque

amount_money_size = [int(x) for x in input().split()]
price_size = deque([int(x) for x in input().split()])
food_count = 0

while amount_money_size and price_size:
    current_amount_money = amount_money_size.pop()
    current_price_size = price_size.popleft()

    if current_amount_money == current_price_size:
        food_count += 1

    elif current_amount_money > current_price_size:
        food_count += 1
        diff = current_amount_money - current_price_size
        if amount_money_size:
            amount_money_size[-1] += diff


if food_count == 0:
    print("Henry remained hungry. He will try next weekend again.")
elif food_count < 4:
    if food_count == 1:
        print(f"Henry ate: {food_count} food.")
    else:
        print(f"Henry ate: {food_count} foods.")
else:
    print(f"Gluttony of the day! Henry ate {food_count} foods.")