from collections import deque

worm_size = deque([int(x) for x in input().split()])
hole_size = deque([int(x) for x in input().split()])
matches = 0
no_matches = 0

while True:
    if len(worm_size) == 0 or len(hole_size) == 0:
        break
    current_worm = worm_size.pop()
    current_hole = hole_size.popleft()

    if current_worm != current_hole:
        current_worm -= 3
        no_matches += 1
        if current_worm > 0:
            worm_size.append(current_worm)
    else:
        matches += 1

if matches > 0:
    print(f"Matches: {matches}")
else:
    print("There are no matches.")
if len(worm_size) == 0:
    if no_matches == 0:
        print("Every worm found a suitable hole!")
    else:
        print("Worms left: none")
else:
    print(f"Worms left:", ", ".join([str(x) for x in worm_size]))  #print(f"Orders left:", *orders)  # " ".join([str(x) for x in orders])
if len(hole_size) == 0:
    print("Holes left: none")
else:
    print(f"Holes left:", ", ".join([str(x) for x in hole_size]))