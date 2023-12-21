numbers = tuple(float(num) for num in input().split())
numbers_data = {}

for num in numbers:
    if num not in numbers_data.keys():
        numbers_data[num] = 0
    numbers_data[num] += 1

for key, value in numbers_data.items():
    print(f"{key} - {value} times")