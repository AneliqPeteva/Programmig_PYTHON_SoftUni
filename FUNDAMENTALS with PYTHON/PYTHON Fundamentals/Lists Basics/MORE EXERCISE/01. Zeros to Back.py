list_number = list(map(int, input().strip().split(", ")))
for element in list_number:
    list_number.append(list_number.pop(list_number.index(0)))
print(list_number)