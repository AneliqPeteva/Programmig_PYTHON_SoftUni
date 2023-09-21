start_number = int(input())
end_number = int(input())
magic_number = int(input())
counter_all_combination = 0
is_found = False

for num_1 in range(start_number, end_number +1):
    for num_2 in range(start_number, end_number + 1):
        counter_all_combination +=1
        if num_1 + num_2 == magic_number:
            print(f"Combination N:{counter_all_combination} ({num_1} + {num_2} = {magic_number})")
            is_found = True
            break
    if is_found:
        break

if num_1 + num_2 != magic_number:
    print(f"{counter_all_combination} combinations - neither equals {magic_number}")