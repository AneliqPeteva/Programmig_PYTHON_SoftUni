data = input().split("|")

sub_list = []

for string in data[::-1]:
    sub_list.extend(string.split())


print(*sub_list)



