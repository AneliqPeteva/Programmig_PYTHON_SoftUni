#string_text = input()
#string_list = string_text.split(" ")
#new_number_list = list()
#for word in string_list:
#    number = int(word)
#    if number < 0:
#        number = abs(number)
#        new_number_list.append(number)
#    else:
#        number = -number
#        new_number_list.append(number)
#
#print(new_number_list)

list_of_number = input().split()
opposite_number = []
for element in list_of_number:
    current_number = -int(element)
    opposite_number.append(current_number)
print(opposite_number)


