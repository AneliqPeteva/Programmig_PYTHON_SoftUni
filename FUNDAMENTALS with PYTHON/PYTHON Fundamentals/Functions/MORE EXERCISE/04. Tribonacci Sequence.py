
def tribonacci(num):
    list = [1, 0, 0]
    for i in range(num):
        next_num = sum(list)
        print(next_num, end=" ")
        list.append(next_num)
        list.pop(0)

number = int(input())

tribonacci(number)