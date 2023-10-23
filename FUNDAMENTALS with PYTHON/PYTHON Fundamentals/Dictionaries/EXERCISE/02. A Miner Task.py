collect_of_resource = {}
while True:
    current_resource = input()
    if current_resource == "stop":
        break
    current_quantity = int(input())
    if current_resource not in collect_of_resource:
        collect_of_resource[current_resource] = 0
    collect_of_resource[current_resource] += current_quantity

for resource, quantity in collect_of_resource.items():
    print(f"{resource} -> {quantity}")