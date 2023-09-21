# Read user input
count_of_group = int(input())

total_count_people = 0
count_group_1 = 0
count_group_2 = 0
count_group_3 = 0
count_group_4 = 0
count_group_5 = 0
# Logic
for i in range(count_of_group):
    count_people_of_group = int(input())
    total_count_people += count_people_of_group
    if count_people_of_group <=5:
        count_group_1 += count_people_of_group
    elif count_people_of_group <= 12:
        count_group_2 += count_people_of_group
    elif count_people_of_group <= 25:
        count_group_3 += count_people_of_group
    elif count_people_of_group <= 40:
        count_group_4 += count_people_of_group
    elif count_people_of_group >= 41:
        count_group_5 += count_people_of_group

percent_1 = (count_group_1 / total_count_people) * 100
percent_2 = (count_group_2 / total_count_people) * 100
percent_3 = (count_group_3 / total_count_people) * 100
percent_4 = (count_group_4 / total_count_people) * 100
percent_5 = (count_group_5 / total_count_people) * 100

# Print output
print(f"{percent_1:.2f}%")
print(f"{percent_2:.2f}%")
print(f"{percent_3:.2f}%")
print(f"{percent_4:.2f}%")
print(f"{percent_5:.2f}%")