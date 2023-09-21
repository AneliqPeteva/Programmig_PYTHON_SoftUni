# Read user input
count_students = int(input())
count_1 = 0
count_2 = 0
count_3 = 0
count_4 = 0
all_grade = 0
# Logic
for i in range(count_students):
    grades = float(input())
    all_grade += grades
    if grades <= 2.99:
        count_1 += 1
    elif grades <= 3.99:
        count_2 += 1
    elif grades <= 4.99:
        count_3 += 1
    elif grades >= 5:
        count_4 += 1
percent_p1 = count_1/count_students * 100
percent_p2 = count_2/count_students * 100
percent_p3 = count_3/count_students * 100
percent_p4 = count_4/count_students * 100
# Print output
print(f"Top students: {percent_p4:.2f}%")
print(f"Between 4.00 and 4.99: {percent_p3:.2f}%")
print(f"Between 3.00 and 3.99: {percent_p2:.2f}%")
print(f"Fail: {percent_p1:.2f}%")
print(f"Average: {all_grade/count_students:.2f}")