# Read user
money_for_excursion = float(input())
currently_money = float(input())
total_day = 0
day_spend = 0

# Logic
while currently_money < money_for_excursion:
    if day_spend >= 5:
        break
    type_of_action = input()
    amount = float(input())
    total_day += 1
    if type_of_action == "spend":
        currently_money -= amount
        day_spend += 1
        if currently_money < 0:
            currently_money = 0
    elif type_of_action == "save":
        day_spend = 0
        currently_money += amount


if day_spend == 5:
    print(f"You can't save the money.")
    print(f"{total_day}")
else:
    print(f"You saved the money for {total_day} days.")


# Print output