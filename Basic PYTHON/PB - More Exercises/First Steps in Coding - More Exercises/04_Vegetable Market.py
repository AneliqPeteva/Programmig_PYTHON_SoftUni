price_vegetables = float(input())
price_fruit = float(input())
total_vegetables = int(input())
total_fruit = int(input())
eu = 1.94

all_price_vegetables = price_vegetables  *total_vegetables
all_price_fruit = price_fruit * total_fruit
all_sum = (all_price_fruit + all_price_vegetables) / eu
print(f"{all_sum:.2f}")