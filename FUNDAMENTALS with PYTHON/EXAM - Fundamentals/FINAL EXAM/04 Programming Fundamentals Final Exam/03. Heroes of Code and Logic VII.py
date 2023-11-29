number_of_heroes = int(input())
max_hp = 100
max_mp = 200

dict_heroes = {}

for current_hero in range(number_of_heroes):
    data_input = input(). split()
    hero_name, hp, mp = data_input[0], int(data_input[1]), int(data_input[2])
    dict_heroes[hero_name] = {"hp": hp, "mp": mp}

data = input().split(" - ")
command = data[0]
while command != "End":
    if command == "CastSpell":
        hero_name, mp_needed, spell_name = data[1], int(data[2]), data[3]
        if dict_heroes[hero_name]["mp"] >= mp_needed:
            dict_heroes[hero_name]["mp"] -= mp_needed
            print(f"{hero_name} has successfully cast {spell_name} and now has {dict_heroes[hero_name]['mp']} MP!")
        else:
            print(f"{hero_name} does not have enough MP to cast {spell_name}!")
    elif command == "TakeDamage":
        hero_name, damage, attacker = data[1], int(data[2]), data[3]
        dict_heroes[hero_name]["hp"] -= damage
        if dict_heroes[hero_name]["hp"] > 0:
            print(f"{hero_name} was hit for {damage} HP by {attacker} and now has {dict_heroes[hero_name]['hp']} HP left!")
        else:
            print(f"{hero_name} has been killed by {attacker}!")
            del dict_heroes[hero_name]
    elif command == "Recharge":
        hero_name, amount = data[1], int(data[2])
        if dict_heroes[hero_name]["mp"] + amount > max_mp:
            amount_recovered = max_mp - dict_heroes[hero_name]["mp"]
            dict_heroes[hero_name]["mp"] = max_mp
            print(f"{hero_name} recharged for {amount_recovered} MP!")
        else:
            dict_heroes[hero_name]["mp"] += amount
            print(f"{hero_name} recharged for {amount} MP!")
    elif command == "Heal":
        hero_name, amount = data[1], int(data[2])
        if dict_heroes[hero_name]["hp"] + amount > max_hp:
            amount_recovered = max_hp - dict_heroes[hero_name]["hp"]
            dict_heroes[hero_name]["hp"] = max_hp
            print(f"{hero_name} healed for {amount_recovered} HP!")
        else:
            dict_heroes[hero_name]["hp"] += amount
            print(f"{hero_name} healed for {amount} HP!")
    data = input().split(" - ")
    command = data[0]

for hero_name, values in dict_heroes.items():
    print(f"{hero_name}\n  HP: {dict_heroes[hero_name]['hp']}\n  MP: {dict_heroes[hero_name]['mp']}")