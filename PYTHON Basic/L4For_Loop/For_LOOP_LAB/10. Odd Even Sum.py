# Read user input
n = int(input())
odd_sum = 0
even_sum = 0

# Logic  - > i е брояча
for i in range(n):
    num = int(input())
    if i % 2 == 0:
        odd_sum += num
    else:
        even_sum += num

# Print output
if even_sum == odd_sum:
    print(f"Yes")
    print(f"Sum = {even_sum}")
else:
    diff = abs(even_sum - odd_sum)
    print(f"No")
    print(f"Diff = {diff}")
