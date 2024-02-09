def shop_from_grocery_list(budgets:int, grocery_list:list, *args):
    buy_products = []
    for name, price in args:
        if name in grocery_list:
            if budgets >= price:
                buy_products.append(name)
                budgets -= price
                grocery_list.remove(name)
            else:
                break
    if grocery_list:
        return f"You did not buy all the products. Missing products: {', '.join(grocery_list)}."
    return f"Shopping is successful. Remaining budget: {budgets:.2f}."



print(shop_from_grocery_list(
    100,
    ["tomato", "cola"],
    ("cola", 5.8),
    ("tomato", 10.0),
    ("tomato", 20.45),
))
print(shop_from_grocery_list(
    100,
    ["tomato", "cola", "chips", "meat"],
    ("cola", 5.8),
    ("tomato", 10.0),
    ("meat", 22),
))
print(shop_from_grocery_list(
    100,
    ["tomato", "cola", "chips", "meat", "chocolate"],
    ("cola", 15.8),
    ("chocolate", 30),
    ("tomato", 15.85),
    ("chips", 50),
    ("meat", 22.99),
))
