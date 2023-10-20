stock = {}

input_line = input()

while input_line != "statistics":
    product, quantity = input_line.split(": ")
    quantity = int(quantity)

    if product in stock:
        stock[product] += quantity
    else:
        stock[product] = quantity
    input_line = input()

count_all_products = len(stock)
sum_all_quantities = sum(stock.values())

print("Products in stock:")
for product, quantity in stock.items():
    print(f"- {product}: {quantity} ")
print(f"Total Products: {count_all_products}")
print(f"Total Quantity: {sum_all_quantities}")

