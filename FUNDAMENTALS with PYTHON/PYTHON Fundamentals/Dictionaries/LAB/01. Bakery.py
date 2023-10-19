elements = input().split()

bakery = {}
for current_index in range(0, len(elements), 2):
    product = elements[current_index]
    quantity = int(elements[current_index + 1])
    bakery[product] = quantity
print(bakery)