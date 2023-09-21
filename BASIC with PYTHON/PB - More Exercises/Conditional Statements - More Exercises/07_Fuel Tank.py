'''
# Read user input
fuel = input()
liters_fuel = float(input())

# Logic
# Print output
if fuel == "Diesel":
    if liters_fuel >= 25:
        print(f"You have enough diesel.")
    else:
        print(f"Fill your tank with diesel!")
elif fuel == "Gasoline":
    if liters_fuel >= 25:
        print(f"You have enough gasoline.")
    else:
        print(f"Fill your tank with gasoline!")
elif fuel == "Gas":
    if liters_fuel >= 25:
        print(f"You have enough gas.")
    else:
        print(f"Fill your tank with gas!")
else:
    print("Invalid fuel!")
'''


'''
# Read user input
fuel = input()
liters_fuel = float(input())

# Logic
# Print output
if fuel == "Diesel" or fuel == "Gas" or fuel == "Gasoline":
    if liters_fuel >= 25:
        print(f"You have enough {fuel.lower()}.")
    else:
        print(f"Fill your tank with {fuel.lower()}!")
else:
    print("Invalid fuel!")
'''


# Read user input
fuel = input()
liters_fuel = float(input())

# Logic
# Print output
if fuel in ("Diesel Gas Gasoline"):
    if liters_fuel >= 25:
        print(f"You have enough {fuel.lower()}.")
    else:
        print(f"Fill your tank with {fuel.lower()}!")
else:
    print("Invalid fuel!")