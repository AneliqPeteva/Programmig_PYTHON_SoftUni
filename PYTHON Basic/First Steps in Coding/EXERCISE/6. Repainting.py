quantity_nylon = int(input())
quantity_paint = int(input())
quantity_diluent = int (input())
all_hours = int (input())

price_nylon = 1.50
price_paint = 14.50
price_diluent = 5.00

sum_nylon = (quantity_nylon + 2) * price_nylon
sum_paint = (quantity_paint + (quantity_paint)*10/100) * price_paint
sum_diluent = quantity_diluent * price_diluent
sum_bags = 0.40
all_sum_materials = sum_nylon + sum_paint + sum_bags + sum_diluent
sum_master_1h = all_sum_materials *30/100
sum_all_master = sum_master_1h * all_hours
total_sum = sum_all_master + all_sum_materials

print(total_sum)
