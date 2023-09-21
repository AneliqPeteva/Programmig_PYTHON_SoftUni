# Read user input
product = input()
town = input()
quantity = float(input())
sum = 0

# Logic
if town == "Sofia":
    if product == "coffee":
       sum = quantity * 0.50
    elif product == "water":
        sum = quantity * 0.80
    elif product == "beer":
        sum = quantity * 1.20
    elif product == "sweets":
        sum = quantity * 1.45
    elif product == "peanuts":
        sum = quantity * 1.60
elif town == "Plovdiv":
    if product == "coffee":
       sum = quantity * 0.40
    elif product == "water":
        sum = quantity * 0.70
    elif product == "beer":
        sum = quantity * 1.15
    elif product == "sweets":
        sum = quantity * 1.30
    elif product == "peanuts":
        sum = quantity * 1.50
elif town == "Varna":
    if product == "coffee":
       sum = quantity * 0.45
    elif product == "water":
        sum = quantity * 0.70
    elif product == "beer":
        sum = quantity * 1.10
    elif product == "sweets":
        sum = quantity * 1.35
    elif product == "peanuts":
        sum = quantity * 1.55
# Print output
print(sum)