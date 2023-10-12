numbers = [int(number) for number in input().split(", ")]
current_group_of_numbers = 10
while numbers: #len(numbers) > 0
    filtered_list = []
    for current_number in numbers:
        if current_number <= current_group_of_numbers:
            filtered_list.append(current_number)
    print(f"Group of {current_group_of_numbers}'s: {filtered_list}")
    numbers = [num for num in numbers if num not in filtered_list]
    current_group_of_numbers += 10

