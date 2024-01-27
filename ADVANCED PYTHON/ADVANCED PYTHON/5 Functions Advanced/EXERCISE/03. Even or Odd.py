def even_odd(*args):
    command = args[-1]

    if command == "even":
        return [a for a in args[:-1] if a % 2 == 0]
    else:
        return [a for a in args[:-1] if a % 2 != 0]



print(even_odd(1, 2, 3, 4, 5, 6, "even"))
print(even_odd(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "odd"))
