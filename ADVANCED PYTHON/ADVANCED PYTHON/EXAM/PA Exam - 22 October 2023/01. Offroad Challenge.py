from collections import deque

initial_fuel = deque([int(x) for x in input().split()])
consumption_indexes = deque([int(x) for x in input().split()])
quantities_needed = deque([int(x) for x in input().split()])
counter = 0
counter_list = []

while initial_fuel:

    current_fuel = initial_fuel.pop()
    current_index = consumption_indexes.popleft()
    check_the_result = current_fuel - current_index

    current_quantity = quantities_needed.popleft()
    if check_the_result < current_quantity:
        print(f"John did not reach: Altitude {counter + 1}")
        if counter == 0:
            print("John failed to reach the top.\nJohn didn't reach any altitude.")
        else:
            print(f"John failed to reach the top.")
            print(f"Reached altitudes:", end=' ')
            print(", ".join(counter_list))
        break
    else:
        counter += 1
        counter_list.append(f"Altitude {counter}")
        print(f"John has reached: Altitude {counter}")
else:
    print("John has reached all the altitudes and managed to reach the top!")





