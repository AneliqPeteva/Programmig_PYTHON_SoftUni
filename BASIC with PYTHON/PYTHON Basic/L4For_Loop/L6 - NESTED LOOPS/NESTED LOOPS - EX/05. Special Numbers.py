start_number = 1111
end_number = 9999
n = int(input())

for i in range(start_number, end_number + 1):
    i = str(i)
    first_num_i = int(i[0])
    second_num_i = int(i[1])
    third_num_i = int(i[2])
    four_num_i = int(i[3])
    if "0" not in i:
        if n % first_num_i == 0 and n % second_num_i == 0 and n % third_num_i == 0 and n % four_num_i == 0:
            print(i, end= " ")
