# Read user input
user_number = int(input())
currently_sum = 0

# Logic
while currently_sum < user_number:
    num = int(input())
    currently_sum += num

# Print output
print(currently_sum)