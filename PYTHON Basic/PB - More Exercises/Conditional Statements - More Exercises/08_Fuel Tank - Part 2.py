# Read user input
type_fuel = input()
liters_fuel = float(input())
club_card = input()

gasoline_for_litre = 2.22
diesel_for_litre = 2.33
gas_for_litre = 0.93

sum_fuel = 0

# Logic
if type_fuel == "Gasoline":
    if club_card == "Yes":
        sum_fuel = liters_fuel * (gasoline_for_litre - 0.18)
    else:
        sum_fuel = liters_fuel * gasoline_for_litre
elif type_fuel == "Diesel":
    if club_card == "Yes":
        sum_fuel = liters_fuel * (diesel_for_litre - 0.12)
    else:
        sum_fuel = liters_fuel * diesel_for_litre
elif type_fuel == "Gas":
    if club_card == "Yes":
        sum_fuel = liters_fuel * (gas_for_litre - 0.08)
    else:
        sum_fuel = liters_fuel * gas_for_litre

if 20 <= liters_fuel <= 25:
    sum_fuel -= sum_fuel * 8 / 100
elif liters_fuel > 25:
    sum_fuel -= sum_fuel * 10 / 100

# Print output
print(f"{sum_fuel:.2f} lv.")