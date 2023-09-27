list_number = input().split()
skip_number_k = int(input())
new_number_executed = []
skip_number_k = skip_number_k - 1
len_list = len(list_number)
index = 0
while len_list > 0:
    index = (skip_number_k + index) % len_list
    new_number_executed.append(list_number.pop(index))
    len_list -= 1

print(f"[{','.join(new_number_executed)}]")


