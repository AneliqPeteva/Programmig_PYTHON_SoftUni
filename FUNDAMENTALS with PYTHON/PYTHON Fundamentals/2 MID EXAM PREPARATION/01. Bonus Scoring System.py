from math import ceil

numbers_of_students = int(input())
number_of_the_lectures = int(input())
bonus = int(input())
total_bonus = 0
max_attendance = 0
for current_student in range(numbers_of_students):
    attendance_of_each_student = int(input())
    max_attendance = max(max_attendance, attendance_of_each_student)
if number_of_the_lectures > 0:
    total_bonus = (max_attendance) / number_of_the_lectures * (5 + bonus)

print(f"Max Bonus: {ceil(total_bonus)}.")
print(f"The student has attended {max_attendance} lectures.")


