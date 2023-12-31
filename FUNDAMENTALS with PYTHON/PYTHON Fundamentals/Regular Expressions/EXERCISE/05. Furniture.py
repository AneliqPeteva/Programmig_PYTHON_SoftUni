import re

main_string = input()

pattern = re.compile(
    r">>(?P<furniture_name>[A-Za-z]+)<<(?P<price>[0-9]+[\.0-9]*)!(?P<quantity>[0-9]+)")

total_money_spend = 0
print("Bought furniture:")
while main_string != "Purchase":
    result = re.finditer(pattern, main_string)
    for show in result:
        total_money_spend += float(show["price"]) * float(show["quantity"])
        print(show["furniture_name"])
    main_string = input()

print(f"Total money spend: {total_money_spend:.2f}")

# import re
#
# bought_furniture = []
# total_cost = 0
# pattern = r">>([A-Za-z]+)<<(\d+\.?\d*)!(\d+)"
# command = input()
# while command != "Purchase":
#     match = re.search(pattern, command)
#     if match:
#         furniture, price, quantity = match.groups()
#         bought_furniture.append(furniture)
#         total_cost += float(price) * int(quantity)
#     command = input()
# print("Bought furniture:")
# for furniture in bought_furniture:
#     print(furniture)
# print(f"Total money spend: {total_cost:.2f}")