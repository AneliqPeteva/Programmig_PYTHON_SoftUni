def add_lesson(list_lessons, title):
    if title not in list_lessons:
        list_lessons.append(title)
    return list_lessons
def insert_lesson(list_lessons, title, index):
    if title not in list_lessons:
        list_lessons.insert(index, title)
    return list_lessons
def remove_lesson(list_lessons, title):
    if title in list_lessons:
        index_lesson_title = list_lessons.index(title)
        if index_lesson_title + 1 in range(len(list_lessons)):
            if "Exercise" in list_lessons[index_lesson_title + 1]:
                list_lessons.pop(index_lesson_title + 1)
        list_lessons.remove(title)
    return list_lessons

def swap_lesson(list_lessons, first_title, second_title):
    if first_title in list_lessons and second_title in list_lessons:
        index_first_title = list_lessons.index(first_title)
        index_second_title = list_lessons.index(second_title)
        first_has_exercise = False
        second_has_exercise = False
        if index_first_title + 1 in range(len(list_lessons)):
            first_has_exercise = "Exercise" in list_lessons[index_first_title + 1]
        if index_second_title + 1 in range(len(list_lessons)):
            second_has_exercise = "Exercise" in list_lessons[index_second_title + 1]
        list_lessons[index_first_title], list_lessons[index_second_title] = list_lessons[index_second_title], \
        list_lessons[index_first_title]
        if first_has_exercise and second_has_exercise:
            list_lessons[index_first_title + 1], list_lessons[index_second_title + 1] = list_lessons[index_second_title + 1], \
                list_lessons[index_first_title + 1]
        elif not first_has_exercise and second_has_exercise:
            lessons.insert(index_first_title + 1, list_lessons.pop(index_second_title + 1))
        if first_has_exercise and not second_has_exercise:
            lessons.insert(index_second_title + 1, list_lessons.pop(index_first_title + 1))
    return list_lessons

def exercise(list_lessons, title):
    if title in list_lessons and f"{title}-Exercise" not in list_lessons:
        index_lesson_title = list_lessons.index(title)
        list_lessons.insert(index_lesson_title + 1, f"{title}-Exercise")
    elif title not in list_lessons:
        list_lessons.append(title)
        list_lessons.append(f"{title}-Exercise")
    return list_lessons


lessons = input().split(", ")
command = input()
while command != "course start":
    command = command.split(":")
    command_type, lesson_title = command[0], command[1]
    if len(command) > 2:
        index_or_lesson_title = command[2]
    if command_type == "Add":
        lessons = add_lesson(lessons, lesson_title)
    elif command_type == "Insert":
        lessons = insert_lesson(lessons, lesson_title, int(index_or_lesson_title))
    elif command_type == "Remove":
        lessons = remove_lesson(lessons, lesson_title)
    elif command_type == "Swap":
        lessons = swap_lesson(lessons, lesson_title, index_or_lesson_title)
    elif command_type == "Exercise":
        lessons = exercise(lessons, lesson_title)

    command = input()

for index, lesson_name in enumerate(lessons):
    print(f"{index + 1}.{lesson_name}")






