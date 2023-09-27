#factor = int(input())
#count = int(input())
#my_list = list()
#length_my_list = count
#
#for num in range(factor, (factor * count) + 1):
#    if num % factor == 0:
#        my_list.append(num)
#    if len(my_list) == length_my_list:
#        break
#my_list.sort()
#print(my_list)

factor = int(input())
count = int(input())
list_of_numbers = []
for multiplier in range(1, count + 1):
    list_of_numbers.append((factor * multiplier))
print(list_of_numbers)

