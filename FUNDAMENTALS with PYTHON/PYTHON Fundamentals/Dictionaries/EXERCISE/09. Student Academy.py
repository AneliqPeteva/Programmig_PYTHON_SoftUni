number = int(input())
students = {}

for current_student in range(number):
    name_student = input()
    grade_student = float(input())
    if name_student not in students:
        students[name_student] = []
    students[name_student].append(grade_student)

for current_name, grade in students.items():
    average = sum(students[current_name]) / len(students[current_name])
    if average >= 4.50:
        print(f"{current_name} -> {average:.2f}")