user_input = input()
prime_sum = 0
non_prime_sum = 0


while user_input != "stop":
    current_num = int(user_input)
    counter = 0

    if current_num < 0:
        print("Number is negative.")
        user_input = input()
        continue

    if current_num == 0:
        user_input = input()
        continue

    for num in range(1, current_num + 1):
        if current_num % num == 0:
            counter += 1

    if counter == 2:
        prime_sum += current_num
    else:
        non_prime_sum += current_num
    user_input = input()

print(f"Sum of all prime numbers is: {prime_sum}")
print(f"Sum of all non prime numbers is: {non_prime_sum}")
