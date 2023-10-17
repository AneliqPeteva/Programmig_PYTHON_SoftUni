def urgent(product):
    if product not in initial_list:
        initial_list.insert(0, product)
    return initial_list
def unnecessary(product):
    if product in initial_list:
        initial_list.remove(product)
    return initial_list

def correct(old_product, new_product):
    if old_product in initial_list:
        old_product_index = initial_list.index(old_product)
        initial_list.insert(old_product_index, new_product)
        initial_list.remove(old_product)
    return initial_list

def rearrange(product):
    if product in initial_list:
        product_index = initial_list.index(product)
        initial_list.append(initial_list.pop(product_index))
    return initial_list

initial_list = input().split("!")
command = input()

while command != "Go Shopping!":
    command = command.split()
    command_type = command[0]
    item = command[1]
    if len(command) > 2:
        old_item = item
        new_item = command[2]
    if command_type == "Urgent":
        initial_list = urgent(item)
    elif command_type == "Unnecessary":
        initial_list = unnecessary(item)
    elif command_type == "Correct":
        old_item = command[1]
        new_item = command[2]
        initial_list = correct(old_item, new_item)
    elif command_type == "Rearrange":
        initial_list = rearrange(item)

    command = input()
print(*initial_list, sep=", ")

