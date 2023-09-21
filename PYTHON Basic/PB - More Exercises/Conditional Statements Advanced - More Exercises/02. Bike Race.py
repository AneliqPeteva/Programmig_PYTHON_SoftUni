# Read user input
count_juniors_group = int(input())
count_seniors_group = int(input())
type_route = input()

# Logic
if type_route == "trail":
    money_juniors = count_juniors_group * 5.50
    money_seniors = count_seniors_group * 7.00
    all_sum_fee = money_seniors + money_juniors
elif type_route == "cross-country":
    money_juniors = count_juniors_group * 8.00
    money_seniors = count_seniors_group * 9.50
    all_sum_fee = money_seniors + money_juniors
    if (count_seniors_group + count_juniors_group) >= 50:
        all_sum_fee *= 0.75
elif type_route == "downhill":
    money_juniors = count_juniors_group * 12.25
    money_seniors = count_seniors_group * 13.75
    all_sum_fee = money_seniors + money_juniors
elif type_route == "road":
    money_juniors = count_juniors_group * 20.00
    money_seniors = count_seniors_group * 21.50
    all_sum_fee = money_seniors + money_juniors

total_sum = all_sum_fee * 0.95
# Print output
print(f"{total_sum:.2f}")