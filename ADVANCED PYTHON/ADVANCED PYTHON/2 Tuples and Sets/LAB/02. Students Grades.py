data_num = int(input())
student_data = {}

for current_num in range(data_num):
    student_name, grade = input().split()

    if student_name not in student_data.keys():
        student_data[student_name] = []
    student_data[student_name].append(float(grade))

for key, value in student_data.items():
    average_grade = sum(value) / len(value)
    convert_grade_to_str = ' '.join(map(lambda val: f"{val:.2f}", value))
    print(f"{key} -> {convert_grade_to_str} (avg: {average_grade:.2f})")
