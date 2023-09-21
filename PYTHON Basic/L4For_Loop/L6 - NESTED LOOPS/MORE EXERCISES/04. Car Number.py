start_num = int(input())
end_num = int(input())

for i in range(start_num, end_num + 1):
    for j in range(start_num, end_num + 1):
        for k in range(start_num, end_num + 1):
            for l in range(start_num, end_num + 1):
                if ((i % 2 == 0 and l % 2 != 0) or (i % 2 != 0 and l % 2 == 0)) and i > l and ((j + k) % 2) == 0:
                    print(f"{i}{j}{k}{l}", end =" ")

