# Read user input
name = input()
average = 0
fails = 0
student_class = 1

# Logic
while True:
    grade = float(input())
    if grade < 4:
        fails += 1
        if fails >= 2:
            print(f"{name} has been excluded at {student_class} grade")
            break
        continue
    student_class += 1
    average += grade
    if student_class > 12:
        print(f"{name} graduated. Average grade: {average / 12:.2f}")
        break
# Print output