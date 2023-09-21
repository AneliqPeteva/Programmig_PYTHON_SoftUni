# Read user input
count_bottle = int(input())
user_input = input()
number_of_clean_plates = 0
number_of_clean_pots = 0
number_dishwasher = 0
# Logic
amount_of_preparation = count_bottle * 750
while True:
    if user_input == "End":
        break
    number_dishwasher += 1
    user_input = int(user_input)
    if number_dishwasher % 3 == 0:
        preparation_for_pots = user_input * 15
        number_of_clean_pots += user_input
        amount_of_preparation -= preparation_for_pots
    else:
        preparation_for_plates = user_input * 5
        number_of_clean_plates += user_input
        amount_of_preparation -= preparation_for_plates
    if amount_of_preparation < 0:
        break
    user_input = input()

# Print output
if amount_of_preparation >= 0:
    print(f"Detergent was enough!")
    print(f"{number_of_clean_plates} dishes and {number_of_clean_pots} pots were washed.")
    print(f"Leftover detergent {amount_of_preparation} ml.")
else:
    print(f"Not enough detergent, {abs(amount_of_preparation)} ml. more necessary!")

