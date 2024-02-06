from collections import deque

programmer_time = deque([int(x) for x in input().split()])
number_of_tasks = [int(x) for x in input().split()]

darth_vader_ducky = range(0, 61)
thor_ducky = range(61, 121)
big_blue_rubber_ducky = range(121, 181)
small_yellow_rubber_ducky = range(181, 241)

darth_vader_ducky_count = 0
thor_ducky_count = 0
big_blue_rubber_ducky_count = 0
small_yellow_rubber_ducky_count = 0

while programmer_time and number_of_tasks:

    current_time = programmer_time.popleft()
    current_tasks = number_of_tasks.pop()

    current_sum = current_time * current_tasks

    if current_sum in darth_vader_ducky:
        darth_vader_ducky_count += 1

    elif current_sum in thor_ducky:
        thor_ducky_count += 1

    elif current_sum in big_blue_rubber_ducky:
        big_blue_rubber_ducky_count += 1

    elif current_sum in small_yellow_rubber_ducky:
        small_yellow_rubber_ducky_count += 1

    else:
        programmer_time.append(current_time)
        number_of_tasks.append(current_tasks - 2)

print("Congratulations, all tasks have been completed! Rubber ducks rewarded:")
print(f"Darth Vader Ducky: {darth_vader_ducky_count}\nThor Ducky: {thor_ducky_count}\nBig Blue Rubber Ducky: {big_blue_rubber_ducky_count}\nSmall Yellow Rubber Ducky: {small_yellow_rubber_ducky_count}")
