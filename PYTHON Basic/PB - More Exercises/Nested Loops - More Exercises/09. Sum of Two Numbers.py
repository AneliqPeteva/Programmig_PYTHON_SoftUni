start = int(input())
end = int(input())
magic_number = int(input())
counter = 0

for i in range(start, end + 1):
    for j in range(start, end + 1):
        counter += 1
        if i + j == magic_number:
            print(f"Combination N:{counter} ({i} + {j} = {magic_number})")
            exit()

if not (i + j == magic_number):
    print(f"{counter} combinations - neither equals {magic_number}")
