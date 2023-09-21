number = int(input())
capacity_water_tank_liters = 255
sum_litres = 0

for i in range(number):
    water_litres = int(input())

    if (sum_litres + water_litres) > capacity_water_tank_liters:
        print("Insufficient capacity!")
        continue
    sum_litres += water_litres
print(sum_litres)
