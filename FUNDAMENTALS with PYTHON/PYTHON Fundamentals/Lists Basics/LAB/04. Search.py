number = int(input())
word = input()
string_list = []

for i in range(number):
    strings = input()
    string_list.append(strings)

print(string_list)

filtered_string = []

for string in string_list:
    if word in string:
        filtered_string.append(string)

print(filtered_string)
