command = input().split()
product = {}
while command[0] != "buy":

    name, price, quantity = command[0], float(command[1]), int(command[2])
    if name not in product.keys():
        product[name] = [price, quantity]
    else:
        product[name][0] = price
        product[name][1] += quantity
    command = input().split()
for key, value in product.items():
    total_price = value[0] * value[1]
    print(f"{key} -> {total_price:.2f}")