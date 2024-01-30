def softuni_students(*args, **kwargs):
    id_name = {}
    id_courses = {}
    result = ""
    invalid_students = []
    valid_students = {}
    for elements in args:
        name = elements[1]
        id = elements[0]

        if not id in id_name:
            id_name[id] = []
        id_name[id].append(name)

    for id, name_courses in kwargs.items():
        if not id in id_courses:
            id_courses[id] = []
        id_courses[id].append(name_courses)




    for id_for_name, name_people in id_name.items():
        if id_for_name in id_courses:
            if not



print(softuni_students(
    ('id_7', 'Silvester1'),
    ('id_32', 'Katq21'),
    ('id_7', 'The programmer'),
    id_76='Spring Fundamentals',
    id_7='Spring Advanced',
))
