courses = {}
command = input()
while command != "end":
    name_courses, name_student = command.split(" : ")
    if name_courses not in courses:
        courses[name_courses] = []
    courses[name_courses].append(name_student)
    command = input()
for current_courses, names in courses.items():
    print(f"{current_courses}: {len(courses[current_courses])}")
    for current_name in names:
        print(f"-- {current_name}")