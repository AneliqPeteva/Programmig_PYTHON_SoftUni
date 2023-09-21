count_paper = int(input())
count_fabric_rolls = int(input())
glue_litre = float(input())
percent = int(input())

paper = 5.80
fabric = 7.20
glue = 1.20

price_paper = count_paper * paper
price_fabric_rolls = count_fabric_rolls * fabric
price_glue = glue * glue_litre

sum = price_glue + price_paper + price_fabric_rolls
total_sum = sum - (sum * percent / 100)

print(f"{total_sum:.3f}")
