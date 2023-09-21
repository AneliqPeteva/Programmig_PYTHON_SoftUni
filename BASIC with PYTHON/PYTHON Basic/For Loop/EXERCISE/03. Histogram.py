# Read user input
n = int(input())

count_p1 = 0
count_p2 = 0
count_p3 = 0
count_p4 = 0
count_p5 = 0

# Logic
for i in range(n):
    input_number = int(input())
    if input_number < 200:
        count_p1 += 1
    elif input_number <= 399:
        count_p2 += 1
    elif input_number <= 599:
        count_p3 += 1
    elif input_number <= 799:
        count_p4 += 1
    elif input_number >= 800:
        count_p5 += 1

percent_p1 = (count_p1 / n) * 100
percent_p2 = (count_p2 / n) * 100
percent_p3 = (count_p3 / n) * 100
percent_p4 = (count_p4 / n) * 100
percent_p5 = (count_p5 / n) * 100

# Output
print(f"{percent_p1:.2f}%")
print(f"{percent_p2:.2f}%")
print(f"{percent_p3:.2f}%")
print(f"{percent_p4:.2f}%")
print(f"{percent_p5:.2f}%")