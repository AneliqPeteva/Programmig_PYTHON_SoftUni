n = int(input())

for i in range(1, 10):
    for j in range(1, 10):
        for k in range(1, 10):
            for l in range(1, 10):
                sum_1 = i + j
                sum_2 = k + l
                if sum_1 == sum_2 and n % sum_1 == 0:
                    print(f"{i}{j}{k}{l}", end=" ")
