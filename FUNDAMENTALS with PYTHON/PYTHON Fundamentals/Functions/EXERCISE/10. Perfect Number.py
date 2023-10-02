def perfect_number(num):
    sum_num = 0
    for divisor in range(1, num):
        if num % divisor == 0:
            sum_num += divisor

    if sum_num == num:
        return "We have a perfect number!"
    else:
        return "It's not so perfect."

number = int(input())
print(perfect_number(number))