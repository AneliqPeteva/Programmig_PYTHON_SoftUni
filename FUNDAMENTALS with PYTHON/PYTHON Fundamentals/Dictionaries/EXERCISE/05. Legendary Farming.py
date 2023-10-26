list_material = input().split()
dict_material = {
    "shards": 0,
    "fragments": 0,
    "motes": 0,
}
obtained = False
while not obtained:
    for index in range(0, len(list_material), 2):
        key = list_material[index + 1].lower()
        value = int(list_material[index])
        if key not in dict_material.keys():
            dict_material[key] = 0
        dict_material[key] += value
        if dict_material["shards"] >= 250:
            print("Shadowmourne obtained!")
            dict_material["shards"] -= 250
            obtained = True
        elif dict_material["fragments"] >= 250:
            print("Valanyr obtained!")
            dict_material["fragments"] -= 250
            obtained = True
        elif dict_material["motes"] >= 250:
            print("Dragonwrath obtained!")
            dict_material["motes"] -= 250
            obtained = True
        if obtained:
            break
    if obtained:
        break
    list_material = input().split()

for material, quantity in dict_material.items():
    print(f"{material}: {quantity}")
