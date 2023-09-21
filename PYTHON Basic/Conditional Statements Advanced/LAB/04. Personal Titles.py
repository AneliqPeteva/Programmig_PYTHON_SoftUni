# Read user input

age = float(input())
gender = input()
# Logic
if gender == "m":
    if age >= 16:
        print("Mr.")
    else:
        print("Master")
elif gender == "f":
    if age >= 16:
        print("Ms.")
    else:
        print("Miss")


# Print output