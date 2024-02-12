from collections import deque

caffeine = [int(x) for x in input().split(', ')]
energy_drinks = deque([int(x) for x in input().split(', ')])
max_coffeine = 300

while caffeine and energy_drinks:
    current_caffeine = caffeine.pop()
    current_energy_drink = energy_drinks.popleft()

    sum = current_caffeine * current_energy_drink

    if sum <= max_coffeine:
        max_coffeine -= sum
    else:
        energy_drinks.append(current_energy_drink)
        if max_coffeine + 30 > 300:
            continue
        else:
            max_coffeine += 30

if energy_drinks:
    print(f"Drinks left: {', '.join(str(x) for x in energy_drinks)}")
else:
    print("At least Stamat wasn't exceeding the maximum caffeine.")
print(f"Stamat is going to sleep with {300-max_coffeine} mg caffeine.")