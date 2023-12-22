
periodic_table = set()

for element in range(int(input())):
    for current_element in input().split():
        periodic_table.add(current_element)

print(*periodic_table, sep="\n")