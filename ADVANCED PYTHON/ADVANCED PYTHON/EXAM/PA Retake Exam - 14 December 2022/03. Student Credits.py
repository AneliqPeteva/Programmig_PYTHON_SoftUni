MAX_CREDITS = 240


def parse_course(course):
    course_name, course_credits, max_test_points, student_points = course.split('-')
    return course_name, int(course_credits), int(max_test_points), int(student_points)


def calculate_student_credits(max_test_points, student_points, course_credits):
    return student_points / max_test_points * course_credits


def generate_result(total_credits, student_info):
    if total_credits >= MAX_CREDITS:
        result = f'Diyan gets a diploma with {total_credits:.1f} credits.\n'
    else:
        credits_needed = MAX_CREDITS - total_credits
        result = f'Diyan needs {credits_needed:.1f} credits more for a diploma.\n'

    sorted_student_info = sorted(student_info.items(), key=lambda kvp: -kvp[1])
    for name, credits_ in sorted_student_info:
        result += f'{name} - {credits_:.1f}\n'
    return result


def students_credits(*courses):
    student_info = {}
    total_credits = 0

    for course in courses:
        course_name, course_credits, max_test_points, student_points = parse_course(course)
        student_credits = calculate_student_credits(max_test_points, student_points, course_credits)
        student_info[course_name] = student_credits
        total_credits += student_credits

    return generate_result(total_credits, student_info)


print(
    students_credits(
        "Computer Science-12-300-250",
        "Basic Algebra-15-400-200",
        "Algorithms-25-500-490"
    )
)
print()
print(
    students_credits(
        "Discrete Maths-40-500-450",
        "AI Development-20-400-400",
        "Algorithms Advanced-50-700-630",
        "Python Development-15-200-200",
        "JavaScript Development-12-500-480",
        "C++ Development-30-500-405",
        "Game Engine Development-70-100-70",
        "Mobile Development-25-250-225",
        "QA-20-300-300",
    )
)
print()
print(
    students_credits(
        "Python Development-15-200-200",
        "JavaScript Development-12-500-480",
        "C++ Development-30-500-405",
        "Java Development-10-300-150"
    )
)