num1 = int(input())
num2 = int(input())

for i in range(num1, num2 + 1):
    counter = 6
    current_num = i
    even_sum = 0
    odd_sum = 0
    while counter > 0:
        digit = current_num % 10
        if counter % 2 == 0:
            even_sum += digit
        else:
            odd_sum += digit
        current_num = current_num // 10
        counter -= 1
    if even_sum == odd_sum:
        print(i, end=" ")
