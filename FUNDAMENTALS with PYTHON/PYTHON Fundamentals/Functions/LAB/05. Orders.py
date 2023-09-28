product = input()
quantity = int(input())

def calculates_total_price(product, quantity):
    if product == "coffee":
        price = 1.50
    elif product == "coke":
        price = 1.40
    elif product == "water":
        price = 1.00
    elif product == "snacks":
        price = 2.00
    result = price * quantity
    return f"{result:.2f}"

print(calculates_total_price(product, quantity))