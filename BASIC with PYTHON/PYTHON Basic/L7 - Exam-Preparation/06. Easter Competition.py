count_cozunaci = int(input())
max_score = 0
winner = ""
for i in range(count_cozunaci):
    current_score = 0
    name_people = input()
    score_for_cozunac = input()
    while score_for_cozunac != "Stop":
        score_for_cozunac = int(score_for_cozunac)
        current_score += score_for_cozunac
        if max_score < current_score:
            max_score = current_score
            winner = name_people
        score_for_cozunac = input()
    print(f"{name_people} has {current_score} points.")
    if score_for_cozunac == "Stop" and max_score == current_score:
        print(f"{winner} is the new number 1!")

print(f"{winner} won competition with {max_score} points!")
