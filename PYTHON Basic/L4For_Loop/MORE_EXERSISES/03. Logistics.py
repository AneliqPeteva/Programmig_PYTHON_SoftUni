# Read user input
count_cargo = int(input())
all_cargo = 0
sum_van = 0
count_van = 0
sum_truck = 0
count_truck = 0
count_train = 0
sum_train = 0
# Logic
for i in range(count_cargo):
    tonnage_of_cargo = int(input())
    all_cargo += tonnage_of_cargo
    if tonnage_of_cargo <= 3:
        price_van = 200
        sum_van += tonnage_of_cargo * price_van
        count_van += tonnage_of_cargo
    elif tonnage_of_cargo <= 11:
        price_truck = 175
        sum_truck += tonnage_of_cargo * price_truck
        count_truck += tonnage_of_cargo
    elif tonnage_of_cargo >= 12:
        price_train = 120
        sum_train += tonnage_of_cargo * price_train
        count_train += tonnage_of_cargo
total_sum = sum_truck + sum_van + sum_train
percent_van = count_van/all_cargo * 100
percent_truck = count_truck/all_cargo * 100
percent_train = count_train/all_cargo * 100
# Print output
print(f"{total_sum/all_cargo:.2f}")
print(f"{percent_van:.2f}%")
print(f"{percent_truck:.2f}%")
print(f"{percent_train:.2f}%")