
operator = input()
first_number = int(input())
second_number = int(input())

def calculates(operator, first_number, second_number):
    if operator == "multiply":
        return first_number * second_number
    elif operator == "divide":
        return int(first_number / second_number)
    elif operator == "add":
        return first_number + second_number
    elif operator == "subtract":
        return first_number - second_number

print(calculates(operator, first_number, second_number))



#def calculates(operator, first_number, second_number):
#    return {
#        'multiply': first_number * second_number,
#        'divide': int(first_number / second_number),
#        'add': first_number + second_number,
#        'subtract': first_number - second_number
#    }.get(operator, 'Invalid operator')
#
#operator = input()
#first_number = int(input())
#second_number = int(input())
#print(calculates(operator, first_number, second_number))