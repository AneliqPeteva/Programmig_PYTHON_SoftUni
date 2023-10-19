# def add_lesson(list_lessons, title):
#     if title not in list_lessons:
#         list_lessons.append(title)
#     return list_lessons
# def insert_lesson(list_lessons, title, index):
#     if title not in list_lessons:
#         list_lessons.insert(index, title)
#     return list_lessons
# def remove_lesson(list_lessons, title):
#     if title in list_lessons:
#         index_lesson_title = list_lessons.index(title)
#         if index_lesson_title + 1 in range(len(list_lessons)):
#             if "Exercise" in list_lessons[index_lesson_title + 1]:
#                 list_lessons.pop(index_lesson_title + 1)
#         list_lessons.remove(title)
#     return list_lessons
#
# def swap_lesson(list_lessons, first_title, second_title):
#     if first_title in list_lessons and second_title in list_lessons:
#         index_first_title = list_lessons.index(first_title)
#         index_second_title = list_lessons.index(second_title)
#         first_has_exercise = False
#         second_has_exercise = False
#         if index_first_title + 1 in range(len(list_lessons)):
#             first_has_exercise = "Exercise" in list_lessons[index_first_title + 1]
#         if index_second_title + 1 in range(len(list_lessons)):
#             second_has_exercise = "Exercise" in list_lessons[index_second_title + 1]
#         list_lessons[index_first_title], list_lessons[index_second_title] = list_lessons[index_second_title], \
#         list_lessons[index_first_title]
#         if first_has_exercise and second_has_exercise:
#             list_lessons[index_first_title + 1], list_lessons[index_second_title + 1] = list_lessons[index_second_title + 1], \
#                 list_lessons[index_first_title + 1]
#         elif not first_has_exercise and second_has_exercise:
#             lessons.insert(index_first_title + 1, list_lessons.pop(index_second_title + 1))
#         if first_has_exercise and not second_has_exercise:
#             lessons.insert(index_second_title + 1, list_lessons.pop(index_first_title + 1))
#     return list_lessons
#
# def exercise(list_lessons, title):
#     if title in list_lessons and f"{title}-Exercise" not in list_lessons:
#         index_lesson_title = list_lessons.index(title)
#         list_lessons.insert(index_lesson_title + 1, f"{title}-Exercise")
#     elif title not in list_lessons:
#         list_lessons.append(title)
#         list_lessons.append(f"{title}-Exercise")
#     return list_lessons
#
#
# lessons = input().split(", ")
# command = input()
# while command != "course start":
#     command = command.split(":")
#     command_type, lesson_title = command[0], command[1]
#     if len(command) > 2:
#         index_or_lesson_title = command[2]
#     if command_type == "Add":
#         lessons = add_lesson(lessons, lesson_title)
#     elif command_type == "Insert":
#         lessons = insert_lesson(lessons, lesson_title, int(index_or_lesson_title))
#     elif command_type == "Remove":
#         lessons = remove_lesson(lessons, lesson_title)
#     elif command_type == "Swap":
#         lessons = swap_lesson(lessons, lesson_title, index_or_lesson_title)
#     elif command_type == "Exercise":
#         lessons = exercise(lessons, lesson_title)
#
#     command = input()
#
# for index, lesson_name in enumerate(lessons):
#     print(f"{index + 1}.{lesson_name}")


initial_schedule = input().split(', ')
schedule = initial_schedule.copy()
line2 = input()
while line2 != 'course start':
    command = line2.split(':')
    if 'Add' in command:
        if command[1] not in schedule:
            schedule.append(command[1])
    elif 'Insert' in command:
        if command[1] not in schedule:
            schedule.insert(int(command[2]), command[1])
    elif 'Remove' in command:
        if command[1] in schedule:
            schedule.remove(command[1])
            if f'{command[1]}-Exercise' in schedule:
                schedule.remove(f'{command[1]}-Exercise')
    elif 'Swap' in command:
        if command[1] in schedule and command[2] in schedule:
            lesson1_i = schedule.index(command[1])
            lesson2_i = schedule.index(command[2])
            schedule[lesson1_i], schedule[lesson2_i] = schedule[lesson2_i], schedule[lesson1_i]
            for lesson_name, lesson_index in zip([command[1], command[2]], [lesson1_i, lesson2_i]):
                if f"{lesson_name}-Exercise" in schedule:
                    schedule.remove(f"{lesson_name}-Exercise")
                    if lesson_index < schedule.index(lesson_name):
                        schedule.insert(schedule.index(lesson_name), f"{lesson_name}-Exercise")
                    else:
                        schedule.insert(schedule.index(lesson_name) + 1, f"{lesson_name}-Exercise")
    elif 'Exercise' in command:
        if command[1] in schedule and f"{command[1]}-Exercise" not in schedule:
            lesson_i = schedule.index(command[1])
            schedule.insert(lesson_i + 1, f'{command[1]}-Exercise')
        elif command[1] not in schedule:
            schedule.append(command[1])
            schedule.append(f'{command[1]}-Exercise')
    line2 = input()
for i, lesson in enumerate(schedule, 1):
    print(f'{i}.{lesson}')




def handle_course_start(current_schedule, current_exercises):
    for i in range(len(current_schedule)):
        for element in current_exercises:
            if element == current_schedule[i]:
                current_schedule.insert(i + 1, f'{element}-Exercise')

    for i in range(len(current_schedule)):
        print(f"{i + 1}.{current_schedule[i]}")

