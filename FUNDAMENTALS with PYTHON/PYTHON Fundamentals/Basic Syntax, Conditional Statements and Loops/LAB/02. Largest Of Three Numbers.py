number1 = int(input())
number2 = int(input())
number3 = int(input())

if number1 < number3 and number2 < number3:
    print(f"{number3}")
elif number1 < number2 and number3 < number2:
    print(f"{number2}")
else:
    print(f"{number1}")