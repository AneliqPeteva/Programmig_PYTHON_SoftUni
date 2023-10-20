list_students = []
course_to_search = ''

while True:
    input_line = input()

    if ":" not in input_line:
        course_to_search = input_line
        break

    name, ID, course = input_line.split(":")
    list_students.append({"name": name, "ID": ID, "course": course})

for current_student in list_students:
    if course_to_search.startswith(current_student['course'][0:5]):
        print(f"{current_student['name']} - {current_student['ID']}")
