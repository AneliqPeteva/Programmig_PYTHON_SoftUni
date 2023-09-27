#money_as_string = input().split(", ")
#count_of_beggars = int(input())
#money_as_digits = []
#final_sums = []
#for element in money_as_string:
#    money_as_digits.append(int(element))
#start_index = 0
#while start_index < count_of_beggars:
#    sum_for_current_beggars = 0
#    for current_index in range(start_index, len(money_as_digits), count_of_beggars):
#        sum_for_current_beggars += money_as_digits[current_index]
#    final_sums.append(sum_for_current_beggars)
#    start_index +=1
#print(final_sums)

money_as_string = input().split(", ")
count_of_beggars = int(input())
final_sum_list = [0] * count_of_beggars
sum_money = 0
for current_index in range(len(money_as_string)):
    index_of_beggar_in_list = current_index % count_of_beggars
    sum_money = int(money_as_string[current_index])
    final_sum_list[index_of_beggar_in_list] += sum_money
print(final_sum_list)
