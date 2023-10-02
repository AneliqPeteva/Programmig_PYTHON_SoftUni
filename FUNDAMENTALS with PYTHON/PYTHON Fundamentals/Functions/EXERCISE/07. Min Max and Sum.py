list_number = [int(x) for x in input().split()]

for num in list_number:
    minimum_number = min(list_number)
    maximum_number = max(list_number)
    sum_numbers = sum(list_number)

print(f"The minimum number is {minimum_number}")
print(f"The maximum number is {maximum_number}")
print(f"The sum number is: {sum_numbers}")