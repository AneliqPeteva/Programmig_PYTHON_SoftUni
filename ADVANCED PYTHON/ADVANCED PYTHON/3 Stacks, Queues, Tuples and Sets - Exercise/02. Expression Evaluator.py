from functools import reduce
expression = input().split()

index = 0

function = {
    "*": lambda i: reduce(lambda a, b: int(a) * int(b), expression[:i]),
    "+": lambda i: reduce(lambda a, b: int(a) + int(b), expression[:i]),
    "/": lambda i: reduce(lambda a, b: int(a) / int(b), expression[:i]),
    "-": lambda i: reduce(lambda a, b: int(a) - int(b), expression[:i])
}

while index < len(expression):
    element = expression[index]

    if element in "*/+-":
        result = function[element](index)
        [expression.pop(1) for i in range(index)]
        expression[0] = result
        index = 0
    index += 1

print(int(expression[0]))

