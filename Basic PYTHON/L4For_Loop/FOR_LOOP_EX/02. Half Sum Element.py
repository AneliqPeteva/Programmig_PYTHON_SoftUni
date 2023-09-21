# Read user input
n = int(input())
sum_number = 0
max_number = 0
# Logic
for i in range(n):
    input_number = int(input())
    sum_number += input_number
    if i == 0:
        max_number = input_number
    if input_number > max_number:
        max_number = input_number
sum_number = sum_number - max_number
if max_number == sum_number:
    print("Yes")
    print(f"Sum = {max_number}")
else:
    diff = abs(max_number - sum_number)
    print("No")
    print(f"Diff = {diff}")


# Print output