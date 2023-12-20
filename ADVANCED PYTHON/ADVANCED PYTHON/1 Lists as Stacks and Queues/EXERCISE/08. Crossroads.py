from collections import deque

green_window = int(input())
free_window = int(input())

total_car_passed = 0

list_car = deque()
info = input()

while info != "END":
    if info != "green":
        list_car.append(info)

    else:
        current_green_window = green_window

        while current_green_window > 0 and list_car:
            car = list_car.popleft()

            time = current_green_window + free_window

            if len(car) > time:
                print(f"A crash happened!\n{car} was hit at {car[time]}.")
                raise SystemExit

            current_green_window -= len(car)
            total_car_passed += 1

    info = input()


print("Everyone is safe.")
print(f"{total_car_passed} total cars passed the crossroads.")


