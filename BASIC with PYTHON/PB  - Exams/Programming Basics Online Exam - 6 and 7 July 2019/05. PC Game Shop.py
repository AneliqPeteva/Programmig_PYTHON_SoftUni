#User input
count_all_game = int(input())
count_hearthstone = 0
count_fornite = 0
count_overwatch = 0
count_others = 0
#logic
for i in range(count_all_game):
    user_input = input()
    if user_input == "Hearthstone":
        count_hearthstone += 1
    elif user_input == "Fornite":
        count_fornite += 1
    elif user_input == "Overwatch":
        count_overwatch += 1
    else:
        count_others +=1

percent_hearthstone = count_hearthstone / count_all_game * 100
percent_fornite = count_fornite / count_all_game * 100
percent_overwatch = count_overwatch / count_all_game * 100
percent_other = count_others / count_all_game * 100
#print output

print(f"Hearthstone - {percent_hearthstone:.2f}%")
print(f"Fornite - {percent_fornite:.2f}%")
print(f"Overwatch - {percent_overwatch:.2f}%")
print(f"Others - {percent_other:.2f}%")