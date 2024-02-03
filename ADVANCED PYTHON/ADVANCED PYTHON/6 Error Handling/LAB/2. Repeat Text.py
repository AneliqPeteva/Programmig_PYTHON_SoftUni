text = input()

try:
    repeats = int(input())
    print(text * repeats)
except ValueError:
    print("Variable times must be an integer")