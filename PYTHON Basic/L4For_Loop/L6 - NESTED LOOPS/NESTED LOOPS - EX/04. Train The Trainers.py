count_people_of_the_jury = int(input())
user_input = input()
counter_presentation = 0
all_grade = 0
all_average_grade = 0

while user_input != "Finish":
    name_presentation = user_input
    counter_presentation += 1
    sum_grade = 0
    for i in range(1, count_people_of_the_jury + 1):
        grade = float(input())
        sum_grade += grade

    average_grade = sum_grade / count_people_of_the_jury
    all_grade += average_grade
    print(f"{name_presentation} - {average_grade:.2f}.")
    user_input = input()
all_average_grade = all_grade / counter_presentation
print(f"Student's final assessment is {all_average_grade:.2f}." )
