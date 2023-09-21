# Read user input
number_1 = int(input())
number_2 = int(input())
mathematical_operator = input()
result = 0
type_number = ''

# Logic
if mathematical_operator == "+" or mathematical_operator == "-" or mathematical_operator == "*":
    if mathematical_operator == "+":
        result = number_1 + number_2
        if result % 2 == 0:
            type_number = "even"
        else:
            type_number = "odd"
    elif mathematical_operator == "-":
        result = number_1 - number_2
        if result % 2 == 0:
            type_number = "even"
        else:
            type_number = "odd"
    elif mathematical_operator == "*":
        result = number_1 * number_2
        if result % 2 == 0:
            type_number = "even"
        else:
            type_number = "odd"
    print(f"{number_1} {mathematical_operator} {number_2} = {result} - {type_number}")

elif mathematical_operator == "/" and number_2 != 0:
    result = number_1 / number_2
    print(f"{number_1} / {number_2} = {result:.2f}")
elif mathematical_operator == "%" and number_2 != 0:
    result = number_1 % number_2
    print(f"{number_1} % {number_2} = {result}")
elif (mathematical_operator == "/" or mathematical_operator == "%") and number_2 == 0:
    print(f"Cannot divide {number_1} by zero")


# Print output