tail = input()
body = input()
head = (input())

my_list = [tail, body, head]

my_list[0], my_list[-1] = my_list[-1], my_list[0]
print(my_list)
