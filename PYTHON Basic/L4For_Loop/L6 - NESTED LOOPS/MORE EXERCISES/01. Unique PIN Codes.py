end_first_num = int(input())
end_second_num = int(input())
end_third_num = int(input())

for i in range(1, end_first_num + 1):
    for j in range(1, end_second_num + 1):
        for k in range(1, end_third_num + 1):
            if i % 2 == 0 and k % 2 == 0 and (j == 2 or j == 3 or j == 5 or j == 7):
                print(f"{i} {j} {k}")
print()
