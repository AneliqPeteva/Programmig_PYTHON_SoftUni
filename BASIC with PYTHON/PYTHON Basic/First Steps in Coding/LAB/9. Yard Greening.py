area_Landscaping = float(input())

price = 7.61

all_sum = area_Landscaping * price
discount = all_sum * (18/100)
total_sum = all_sum - discount

print(f'The final price is: {total_sum} lv.')
print(f"The discount is: {discount} lv.")