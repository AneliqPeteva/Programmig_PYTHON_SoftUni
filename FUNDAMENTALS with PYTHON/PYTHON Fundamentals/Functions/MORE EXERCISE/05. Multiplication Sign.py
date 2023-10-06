def multiplication_sign(num1, num2, num3):
    list_number = [num1, num2, num3]
    count_negative_numbers = 0
    for num in list_number:
        if num < 0:
            count_negative_numbers += 1
    if num1 == 0 or num2 == 0 or num3 == 0:
        return "zero"
    elif (num1 > 0 and num2 > 0 and num3 > 0) or (count_negative_numbers == 2):
        return "positive"
    elif count_negative_numbers != 2:
        return "negative"

number_1 = int(input())
number_2 = int(input())
number_3 = int(input())

print(multiplication_sign(number_1, number_2, number_3))