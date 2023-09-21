end_100 = int(input())
end_10 = int(input())
end_1 = int(input())

for i in range(1, end_100 + 1):
    for j in range(1, end_10 +1):
        for k in range(1, end_1 +1):
            if i % 2 == 0 and k % 2 == 0 and (j == 2 or j == 3 or j == 5 or j == 7):
                print(f"{i} {j} {k}")
print()