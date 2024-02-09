from collections import deque

textiles = deque([int(x) for x in input().split()])
medicaments = [int(x) for x in input().split()]

new_items = {
    "MedKit": 0,
    "Bandage": 0,
    "Patch": 0,
}

while textiles and medicaments:
    current_textile = textiles.popleft()
    current_medicament = medicaments.pop()
    current_sum = current_medicament + current_textile

    if current_sum == 30:
        new_items["Patch"] += 1

    elif current_sum == 40:
        new_items["Bandage"] += 1

    elif current_sum == 100:
        new_items["MedKit"] += 1

    elif current_sum > 100:
        new_items["MedKit"] += 1
        if medicaments:
            medicaments[-1] += current_sum - 100

    else:
        current_medicament += 10
        medicaments.append(current_medicament)


if not textiles and not medicaments:
    print("Textiles and medicaments are both empty.")
elif not textiles:
    print("Textiles are empty.")
elif not medicaments:
    print("Medicaments are empty.")


sorted_items = sorted(new_items.items(), key=lambda x: (-x[1], x[0]))
for name, count in sorted_items:
    if count > 0:
        print(f"{name} - {count}")

if textiles:
    print(f'Textiles left: {", ".join(map(str, textiles))}')

if medicaments:
    print(f'Medicaments left: {", ".join(map(str, reversed(medicaments)))}')


