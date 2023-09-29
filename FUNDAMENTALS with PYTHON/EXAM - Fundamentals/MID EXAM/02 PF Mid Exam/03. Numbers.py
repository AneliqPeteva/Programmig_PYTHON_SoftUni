list_number = [int(x) for x in input().split()]
list_number.sort(reverse=True)
average_number = sum(list_number) / len(list_number)
top_numbers = []
for num in list_number:
    if num > average_number:
        top_numbers.append(num)

if len(top_numbers) == 0:
    print("No")
elif len(top_numbers) > 5:
    top_numbers = top_numbers[0:5]
    print(*top_numbers)
else:
    print(*top_numbers)


