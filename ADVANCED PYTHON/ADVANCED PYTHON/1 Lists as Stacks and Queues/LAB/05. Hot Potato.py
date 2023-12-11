# from _collections import deque
# name_of_players = input().split()
#
# step_of_hot_potato = int(input())
#
# players_deque = deque(name_of_players)
# count = 0
#
# while len(players_deque) > 1:
#     count += 1
#     current_player = players_deque.popleft()
#
#     if count == step_of_hot_potato:
#         print(f"Removed {current_player}")
#         count = 0
#     else:
#         players_deque.append(current_player)
#
# print(f"Last is {players_deque[0]}")


from _collections import deque
name_of_players = input().split()
step_of_hot_potato = int(input())
players_deque = deque(name_of_players)


while len(players_deque) > 1:
    for i in range(step_of_hot_potato - 1):
        players_deque.append(players_deque.popleft())

    print(f"Removed {players_deque.popleft()}")


print(f"Last is {players_deque.pop()}")

