count_man = int(input())
count_woman = int(input())
max_count_table = int(input())
counter = 0

for man in range(1, count_man +1):
    for woman in range(1, count_woman +1):
        counter += 1
        if counter > max_count_table:
            break
        print(f"({man} <-> {woman})", end= " ")