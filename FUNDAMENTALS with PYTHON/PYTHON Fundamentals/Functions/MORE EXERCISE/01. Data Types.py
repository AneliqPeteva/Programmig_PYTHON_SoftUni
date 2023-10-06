def calc(arg1, arg2):
    if arg1 == "int":
        result = int(arg2) * 2
        return f"{result:.0f}"
    elif arg1 == "real":
        result = float(arg2) * 1.5
        return f"{result:.2f}"
    elif arg1 == "string":
        return f"${arg2}$"

command = input()
number = input()
print(calc(command, number))