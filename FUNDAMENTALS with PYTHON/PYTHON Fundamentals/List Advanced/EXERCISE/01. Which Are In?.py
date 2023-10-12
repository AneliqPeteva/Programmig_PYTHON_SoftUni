first_sequence = input().split(", ")
second_sequence = input().split(", ")
substring_list = []
for first_string in first_sequence:
    for second_string in second_sequence:
        if first_string in second_string:
            substring_list.append(first_string)
            break
print(substring_list)