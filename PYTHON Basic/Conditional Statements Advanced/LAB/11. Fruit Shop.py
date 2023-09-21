# Read user input

fruit = input()
day_of_week = input()
qty = float(input())
result = "error"
# Logic
if day_of_week == "Monday" or day_of_week == "Tuesday" or day_of_week == "Wednesday" or day_of_week == "Thursday" or day_of_week == "Friday":
    if fruit == "banana":
        result = qty * 2.50
    elif fruit == "apple":
        result = qty * 1.20
    elif fruit == "orange":
        result = qty * 0.85
    elif fruit == "grapefruit":
        result = qty * 1.45
    elif fruit == "kiwi":
        result = qty * 2.70
    elif fruit == "pineapple":
        result = qty * 5.50
    elif fruit == "grapes":
        result = qty * 3.85
elif day_of_week == "Saturday" or day_of_week == "Sunday":
    if fruit == "banana":
        result = qty * 2.70
    elif fruit == "apple":
        result = qty * 1.25
    elif fruit == "orange":
        result = qty * 0.90
    elif fruit == "grapefruit":
        result = qty * 1.60
    elif fruit == "kiwi":
        result = qty * 3.00
    elif fruit == "pineapple":
        result = qty * 5.60
    elif fruit == "grapes":
        result = qty * 4.20

# Print output
if result == "error":
    print("error")
else:
    print(f'{result:.2f}')