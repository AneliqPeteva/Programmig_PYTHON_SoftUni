number_of_cars = int(input())
car_info = {}
for current_car in range(number_of_cars):
    car_model, mileage, fuel = input().split("|")
    car_info[car_model] = [int(mileage), int(fuel)]

command = input().split(" : ")
while command[0] != "Stop":
    if command[0] == "Drive":
        car_model = command[1]
        distance = int(command[2])
        fuel = int(command[3])
        if fuel <= car_info[car_model][1]:
            car_info[car_model][1] -= fuel
            car_info[car_model][0] += distance
            print(f"{car_model} driven for {distance} kilometers. {fuel} liters of fuel consumed.")
            if car_info[car_model][0] > 100000:
                print(f"Time to sell the {car_model}!")
                car_info.pop(car_model)
        else:
            print("Not enough fuel to make that ride")

    elif command[0] == "Refuel":
        car_model = command[1]
        fuel = int(command[2])
        if car_info[car_model][1] + fuel > 75:
            diff = 75 - car_info[car_model][1]
            car_info[car_model][1] = 75
            print(f"{car_model} refueled with {diff} liters")
        else:
            car_info[car_model][1] += fuel
            print(f"{car_model} refueled with {fuel} liters")

    elif command[0] == "Revert":
        car_model = command[1]
        kilometers = int(command[2])
        if car_info[car_model][0] - kilometers >= 10000:
            car_info[car_model][0] -= kilometers
            print(f"{car_model} mileage decreased by {kilometers} kilometers")
        else:
            car_info[car_model][0] = 10000


    command = input().split(" : ")

for key, value in car_info.items():
    print(f"{key} -> Mileage: {value[0]} kms, Fuel in the tank: {value[1]} lt.")