all_employees = 3
number_students_for_first_employees = int(input())
number_students_for_second_employees = int(input())
number_students_for_third_employees = int(input())
count_students = int(input())
needed_time = 0
time_for_break_employees = 1
all_answer_per_1_hours = number_students_for_first_employees + number_students_for_second_employees + number_students_for_third_employees
all_time_break = 0

while count_students > all_answer_per_1_hours:
    needed_time += 1
    count_students -= all_answer_per_1_hours
    if needed_time % 3 == 0:
        all_time_break += time_for_break_employees

needed_time += all_time_break

if count_students > 0:
    needed_time += 1
print(f"Time needed: {needed_time}h.")
