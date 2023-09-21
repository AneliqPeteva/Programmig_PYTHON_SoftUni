#read input
from math import ceil, floor

area_vineyard = int(input())
grapes_for_one_square_meter = float(input())
required_liters_of_wine = int(input())
count_of_workers =  int(input())

#logic
total_grapes = area_vineyard * grapes_for_one_square_meter
wine_for_one_liter = 0.4 * (total_grapes / 2.5)

left_wine = ceil(abs(wine_for_one_liter - required_liters_of_wine))
missing_wine = floor(abs(wine_for_one_liter - required_liters_of_wine))

if wine_for_one_liter < required_liters_of_wine:
    print(f"It will be a tough winter! More {missing_wine} liters wine needed.")
else:
    print(f"Good harvest this year! Total wine: {floor(wine_for_one_liter)} liters.")
    print(f"{left_wine} liters left -> {ceil(left_wine / count_of_workers)} liters per person.")
