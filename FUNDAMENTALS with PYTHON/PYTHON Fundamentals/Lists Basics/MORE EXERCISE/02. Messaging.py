#number = input().split(" ")
#input_string = input()
#final_message = ""
#
#for element_num in number:
#    find_index = sum([int(s_num) for s_num in element_num])
#    if find_index >= len(input_string):
#        find_index = find_index - len(input_string)
#    final_message += input_string[find_index]
#    input_string = input_string[:find_index] + input_string[find_index + 1:]
#
#print(final_message)

number = input().split(" ")
input_string = input()
final_message = ""
for element_num in number:
    find_index = 0
    for digit in element_num:
        find_index += int(digit)
    if find_index >= len(input_string):
        find_index = find_index - len(input_string)
    final_message += input_string[find_index]
    input_string = input_string[:find_index] + input_string[find_index + 1:]

print(final_message)
