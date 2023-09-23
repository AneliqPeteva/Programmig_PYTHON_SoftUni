string = input()

my_list = string.split(", ")
check_for_number = len(my_list) - 1

for word in my_list:
    if word == "wolf" and check_for_number == 0:
        text_print = "Please go away and stop eating my sheep"
    elif word == "wolf":
        text_print = f"Oi! Sheep number {check_for_number}! You are about to be eaten by a wolf!"

    check_for_number -= 1
print(text_print)