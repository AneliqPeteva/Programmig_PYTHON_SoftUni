# Read user input
n = int(input())
min_number = 0
max_number = 0

# Logic
for i in range(n):
    num = int(input())
    if i == 0:
        min_number = num
        max_number = num
    else:
        if max_number < num:
            max_number = num
        elif min_number > num:
            min_number = num

# Print output
print(f"Max number: {max_number}")
print(f"Min number: {min_number}")
