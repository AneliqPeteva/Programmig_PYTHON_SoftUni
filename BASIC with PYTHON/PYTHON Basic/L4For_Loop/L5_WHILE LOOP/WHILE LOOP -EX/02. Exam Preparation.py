'''
# Read user input
failed_threshold = int(input())
counter_unsatisfactory_grades = 0
failed_times = 0
grades_sum = 0
last_problem = 0
name_problem = input()
# Logic
while True:
    if name_problem == "Enough":
        print(f"Average score: {grades_sum/failed_times:.2f}")
        print(f"Number of problems: {failed_times}")
        print(f"Last problem: {last_problem}")
        break
    grade = int(input())
    last_problem = name_problem
    failed_times += 1
    grades_sum += grade
    if grade <= 4:
        counter_unsatisfactory_grades +=1
        if counter_unsatisfactory_grades >= failed_threshold:
            print(f"You need a break, {counter_unsatisfactory_grades} poor grades.")
            break
    name_problem = input()
# Print output
'''

failed_threshold = int(input())
counter_unsatisfactory_grades = 0
failed_times = 0
grades_sum = 0
last_problem = 0
name_problem = input()

while name_problem != "Enough":
    grade = int(input())
    failed_times += 1
    grades_sum += grade
    last_problem = name_problem
    if grade <= 4:
        counter_unsatisfactory_grades += 1
    if counter_unsatisfactory_grades >= failed_threshold:
        break

    name_problem = input()

if counter_unsatisfactory_grades == failed_threshold:
    print(f"You need a break, {counter_unsatisfactory_grades} poor grades.")

else:
    print(f"Average score: {grades_sum / failed_times:.2f}")
    print(f"Number of problems: {failed_times}")
    print(f"Last problem: {last_problem}")