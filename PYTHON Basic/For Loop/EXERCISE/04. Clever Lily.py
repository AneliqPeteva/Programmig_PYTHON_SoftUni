# Read user input
currently_years = int(input())
price_wash_machine = float(input())
price_for_one_toys = int(input())
money_for_birthday = 10
saved_money = 0
count_toes = 0
# Logic
for currently_years in range(1, currently_years + 1):
    if currently_years % 2 == 0:
        saved_money += (money_for_birthday - 1)
        money_for_birthday += 10
    else:
        count_toes += 1

sum_toys = count_toes * price_for_one_toys
total_sum = saved_money + sum_toys
# Print output
diff = abs(total_sum - price_wash_machine)
if total_sum >= price_wash_machine:
    print(f"Yes! {diff:.2f}")
else:
    print(f"No! {diff:.2f}")