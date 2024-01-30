def gather_credits(max_credits, *args):
    sum_credits = 0
    courses = []

    for name_course, current_credits in args:
        if sum_credits >= max_credits:
            break
        if name_course not in courses:
            # continue
            courses.append(name_course)
            sum_credits += current_credits


    if sum_credits >= max_credits:
        return f"Enrollment finished! Maximum credits: {sum_credits}.\nCourses: {', '.join(sorted(courses))}"
    return f"You need to enroll in more courses! You have to gather {max_credits - sum_credits} credits more."



print(gather_credits(
    80,
    ("Basics", 27),
))

print(gather_credits(
    80,
    ("Advanced", 30),
    ("Basics", 27),
    ("Fundamentals", 27),
))

print(gather_credits(
    60,
    ("Basics", 27),
    ("Fundamentals", 27),
    ("Advanced", 30),
    ("Web", 30)
))




