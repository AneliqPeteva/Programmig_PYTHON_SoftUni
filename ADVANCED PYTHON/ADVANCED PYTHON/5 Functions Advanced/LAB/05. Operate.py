# from functools import reduce
#
#
# def operate(operator, *args):
#     def add():
#         return reduce(lambda a, b: a + b, args)
#
#     def subtract():
#         return reduce(lambda a, b: a - b, args)
#
#     def multiply():
#         return reduce(lambda a, b: a * b, args)
#
#     def divide():
#         return reduce(lambda a, b: a / b, args)
#
#     if operator == "+":
#         return add()
#     elif operator == "-":
#         return subtract()
#     elif operator == "*":
#         return multiply()
#     elif operator == "/":
#         return divide()
#
#
# print(operate("+", 1, 2, 3))
# print()
# print(operate("*", 3, 4))


from functools import reduce

def operate (operator, *args):
    if operator == "+":
        return reduce(lambda a, b: a + b, args)
    elif operator == "-":
        return reduce(lambda a, b: a - b, args)
    elif operator == "*":
        return reduce(lambda a, b: a * b, args)
    elif operator == "/":
        return reduce(lambda a, b: a / b, args)


print(operate("+", 1, 2, 3))
print(operate("*", 3, 4))
