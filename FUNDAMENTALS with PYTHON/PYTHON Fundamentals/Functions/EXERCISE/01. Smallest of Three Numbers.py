list_num = []
for num in range(3):
    number = int(input())
    list_num.append(number)

def find_smallest_num(list_num):
    result = min(list_num)
    return result

print(find_smallest_num(list_num))
