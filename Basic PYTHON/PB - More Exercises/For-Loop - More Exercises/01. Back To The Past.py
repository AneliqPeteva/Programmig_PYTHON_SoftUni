# Read user input
money = float(input())
year = int(input())
currently_years = 18
money_spent = 0
# Logic
for i in range(1800, year + 1):
    if i % 2 == 0:
        money_spent += 12000
    else:
        money_spent += 12000 + 50 * (18 + (i - 1800))

left_money = abs(money - money_spent)
# Print output
if money_spent < money:
    print(f"Yes! He will live a carefree life and will have {left_money:.2f} dollars left.")
else:
    print(f"He will need {left_money:.2f} dollars to survive.")