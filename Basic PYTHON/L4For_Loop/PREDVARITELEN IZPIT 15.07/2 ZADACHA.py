money_for_day = float(input())
profit = float(input())
expenses = float(input())
price_gift = float(input())

all_money = (5 * money_for_day) + (5 * profit) - expenses

if all_money >= price_gift:
    print(f"Profit: {all_money:.2f} BGN, the gift has been purchased.")
else:
    print(f"Insufficient money: {price_gift - all_money:.2f} BGN.")

