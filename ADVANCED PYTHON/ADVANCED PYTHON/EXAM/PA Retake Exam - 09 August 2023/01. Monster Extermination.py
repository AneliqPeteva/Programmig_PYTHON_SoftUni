from collections import deque

monsters_armors = deque(int(x) for x in input().split(','))
soldiers_strength = [int(x) for x in input().split(',')]

killed_monsters = 0

while monsters_armors and soldiers_strength:
    current_monster_armor = monsters_armors.popleft()
    current_soldier_strength = soldiers_strength.pop()
    if current_soldier_strength >= current_monster_armor:
        killed_monsters += 1
        current_soldier_strength -= current_monster_armor
        if soldiers_strength:
            soldiers_strength[-1] += current_soldier_strength
        elif not soldiers_strength and current_soldier_strength > 0:
            soldiers_strength.append(current_soldier_strength)
    else:
        current_monster_armor -= current_soldier_strength
        monsters_armors.append(current_monster_armor)

if not monsters_armors:
    print('All monsters have been killed!')
if not soldiers_strength:
    print('The soldier has been defeated.')
print(f'Total monsters killed: {killed_monsters}')