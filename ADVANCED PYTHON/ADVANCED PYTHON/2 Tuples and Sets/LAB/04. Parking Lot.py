number = int(input())
car_data = []
for current_car in range(number):
    direction, car_numer = input().split(", ")
    if direction == "IN":
        if car_numer not in car_data:
            car_data.append(car_numer)
    elif direction == "OUT":
        car_data.remove(car_numer)

if car_data:
    for car in car_data:
        print(car)
else:
    print(f"Parking Lot is Empty")
