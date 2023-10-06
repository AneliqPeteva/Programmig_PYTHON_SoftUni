number_students = int(input())
number_lectures = int(input())
additional_bonus = int(input())
max_bonus_point = 0
total_bonus = 0
attendance_current_student = 0
for current_student in range(number_students):
    attendance_of_each_student = int(input())
    total_bonus = attendance_of_each_student / number_lectures * (5 + additional_bonus)
    if total_bonus > max_bonus_point:
        max_bonus_point = total_bonus
        attendance_current_student = attendance_of_each_student
print(f"Max Bonus: {round(max_bonus_point)}.")
print(f"The student has attended {attendance_current_student} lectures.")

