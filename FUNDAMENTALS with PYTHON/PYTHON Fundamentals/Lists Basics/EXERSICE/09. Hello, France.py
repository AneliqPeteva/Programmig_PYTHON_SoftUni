ticket_for_train = 150
collection_of_items = input().split("|")
budget = float(input())
current_budget = budget
profit = 0
new_price_list = []
for item in collection_of_items:
    type_item, price_item = item.split("->")
    price_item = float(price_item)
    price_is_valid = False
    if type_item == "Clothes":
        if price_item <= 50:
            price_is_valid = True
    elif type_item == "Shoes":
        if price_item <= 35:
            price_is_valid = True
    elif type_item == "Accessories":
        if price_item <= 20.50:
            price_is_valid = True
    if price_is_valid:
        if current_budget >= price_item:
            current_budget -= price_item
            new_price_item = price_item * 1.40
            new_price_list.append(new_price_item)
            profit += (new_price_item - price_item)

for new_price in new_price_list:
    print(f"{new_price:.2f}", end= " ")
print()
print(f"Profit: {profit:.2f}")

if (profit + budget) >= ticket_for_train:
    print("Hello, France!" )
else:
    print("Not enough money.")