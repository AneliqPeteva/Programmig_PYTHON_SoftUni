import re

input_string = input()
calories_needed_per_day = 2000
products = {}
total_calories = 0

pattern = r"([#|])([A-Za-z\s]+)\1([0-9]{2}\/[0-9]{2}\/[0-9]{2})\1(\d+)\1"
matches = re.finditer(pattern, input_string)

for match in matches:
    total_calories += int(match.groups()[3])

days = total_calories // calories_needed_per_day

print(f"You have food to last you for: {days} days!")
matches = re.finditer(pattern, input_string)
for match in matches:
    sep, item, expiration_date, calories = match.groups()
    print(f'Item: {item}, Best before: {expiration_date}, Nutrition: {calories}')