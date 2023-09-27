first_row = input().split()
second_row = input().split()
third_row = input().split()

name_player = "First"
found = False

for player in range(1, 3):
    player = str(player)
    line = [player, player, player]
    if line == first_row or line == second_row or line == third_row:
        found = True
    for index in range(0, 3):
        if first_row[index] == player and second_row[index] == player and third_row[index] == player:
            found =True
    if first_row[0] == player and second_row[1] == player and third_row[2] == player:
        found = True
    elif first_row[2] == player and second_row[1] == player and third_row[0] == player:
        found = True
    if found:
        print(f"{name_player} player won")
        break
    name_player = "Second"
else:
    print("Draw!")