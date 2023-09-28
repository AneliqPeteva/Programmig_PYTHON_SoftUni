list_numbers = list(map(float, input().split()))
absolute_value = []
for element in list_numbers:
    absolute_value.append(abs(element))
print(absolute_value)