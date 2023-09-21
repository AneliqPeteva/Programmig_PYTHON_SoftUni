# Read user input
degrees = int(input())
time_of_day = input()
outfit = " "
shoes = " "

# Logic
if 10 <= degrees <= 18:
    if time_of_day == "Morning":
        outfit = "Sweatshirt"
        shoes = "Sneakers"
    elif time_of_day == "Afternoon" or time_of_day == "Evening":
        outfit = "Shirt"
        shoes = "Moccasins"
elif 18 < degrees <= 24:
    if time_of_day == "Morning" or time_of_day == "Evening":
        outfit = "Shirt"
        shoes = "Moccasins"
    elif time_of_day == "Afternoon":
        outfit = "T-Shirt"
        shoes = "Sandals"
elif degrees >= 25:
    if time_of_day == "Morning":
        outfit = "T-Shirt"
        shoes = "Sandals"
    elif time_of_day == "Afternoon":
        outfit = "Swim Suit"
        shoes = "Barefoot"
    elif time_of_day == "Evening":
        outfit = "Shirt"
        shoes = "Moccasins"

# Print output
print(f"It's {degrees} degrees, get your {outfit} and {shoes}.")