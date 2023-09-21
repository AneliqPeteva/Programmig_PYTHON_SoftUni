# Read user input
user_input = int(input())
count_1 = 0
count_2 = 0
count_3 = 0
count_4 = 0
count_5 = 0
count_6 = 0
all_count = 0
result = 0
# Logic
for i in range(user_input):
    num = float(input())
    all_count += 1
    if 0 <= num <= 9:
        count_1 += 1
        result += num * 0.20
    elif 10 <= num <= 19:
        count_2 += 1
        result += num * 0.30
    elif 20 <= num <= 29:
        count_3 += 1
        result += num * 0.40
    elif 30 <= num <= 39:
        count_4 += 1
        result += 50
    elif 40 <= num <= 50:
        count_5 += 1
        result += 100
    else:
        count_6 += 1
        result = result / 2

percent_1 = count_1 / all_count * 100
percent_2 = count_2 / all_count * 100
percent_3 = count_3 / all_count * 100
percent_4 = count_4 / all_count * 100
percent_5 = count_5 / all_count * 100
percent_6 = count_6 / all_count * 100

# Print output
print(f"{result:.2f}")
print(f"From 0 to 9: {percent_1:.2f}%")
print(f"From 10 to 19: {percent_2:.2f}%")
print(f"From 20 to 29: {percent_3:.2f}%")
print(f"From 30 to 39: {percent_4:.2f}%")
print(f"From 40 to 50: {percent_5:.2f}%")
print(f"Invalid numbers: {percent_6:.2f}%")
