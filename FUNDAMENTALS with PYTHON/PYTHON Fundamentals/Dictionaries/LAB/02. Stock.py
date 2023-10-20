stock_data = input().split()

stock = {}

for element in range(0, len(stock_data), 2):
    product = stock_data[element]
    quantity = stock_data[element + 1]
    stock[product] = quantity

product_for_search = input().split()

for product in product_for_search:
    if product in stock.keys():
        print(f"We have {stock[product]} of {product} left")
    else:
        print(f"Sorry, we don't have {product}")