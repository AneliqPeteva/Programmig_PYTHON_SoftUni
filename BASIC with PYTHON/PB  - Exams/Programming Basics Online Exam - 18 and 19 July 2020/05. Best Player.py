max_goals = 0
name_best_player = ""

while True:
    name = input()
    if name == "END":
        break
    number_goals = int(input())
    if max_goals < number_goals:
        max_goals = number_goals
        name_best_player = name

    if number_goals >= 10:
        break

print(f"{name_best_player} is the best player!")
if max_goals < 3:
    print(f"He has scored {max_goals} goals.")
else:
    print(f"He has scored {max_goals} goals and made a hat-trick !!!")