# Read user input
n = int(input())
currently_sum = 0
max_diff = 0
# Logic
for i in range(n):
    num_1 = int(input())
    num_2 = int(input())
    if i > 0:
        if abs(currently_sum - num_1 - num_2) > max_diff:
            max_diff = abs(currently_sum - num_1 - num_2)
    currently_sum = num_1 + num_2
# Print output
if max_diff == 0:
    print(f"Yes, value={currently_sum}")
else:
    print(f"No, maxdiff={max_diff}")