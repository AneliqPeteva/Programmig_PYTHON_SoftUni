from collections import deque

cups = deque([int(c) for c in input().split()])
bottles = deque([int(b) for b in input().split()])

wasted_water = 0

while cups and bottles:
    current_cup = cups.popleft()
    current_bottle = bottles.pop()

    if current_cup <= current_bottle:
        wasted_water += current_bottle - current_cup
    else:
        cups.appendleft(current_cup - current_bottle)

if bottles:
    print(f"Bottles: {' '.join([str(bottle) for bottle in bottles])}")
else:
    print(f"Cups: {' '.join([str(cup) for cup in cups])}")

print(f"Wasted litters of water: {wasted_water}")
