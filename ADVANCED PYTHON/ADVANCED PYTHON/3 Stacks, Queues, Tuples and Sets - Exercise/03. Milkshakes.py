from collections import deque

chocolates = deque(int(x) for x in input().split(", "))
cups_of_milk = deque(int(x) for x in input().split(", "))

count_milkshake = 0

while count_milkshake != 5 and chocolates and cups_of_milk:
    chocolate = chocolates.pop()
    cup_milk = cups_of_milk.popleft()

    if chocolate <= 0 and cup_milk <= 0:
        continue
    elif chocolate <= 0:
        cups_of_milk.appendleft(cup_milk)
        continue
    elif cup_milk <= 0:
        chocolates.append(chocolate)
        continue

    if chocolate == cup_milk:
        count_milkshake += 1
    else:
        cups_of_milk.append(cup_milk)
        chocolate -= 5
        chocolates.append(chocolate)

if count_milkshake == 5:
    print("Great! You made all the chocolate milkshakes needed!")
else:
    print("Not enough milkshakes.")
if chocolates:
    print(f"Chocolate: {', '.join(str(x) for x in chocolates)}")
else:
    print("Chocolate: empty")
if cups_of_milk:
    print(f"Milk: {', '.join(str(x) for x in cups_of_milk)}")
else:
    print("Milk: empty")

