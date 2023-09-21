command = input()

while command != "Welcome!":
    if command == "Voldemort":
        print("You must not speak of that name!")
        break
    length_name = len(command)
    if length_name < 5:
        print(f"{command} goes to Gryffindor.")
    elif length_name == 5:
        print(f"{command} goes to Slytherin.")
    elif length_name == 6:
        print(f"{command} goes to Ravenclaw.")
    else:
        print(f"{command} goes to Hufflepuff.")

    command = input()
else:
    print("Welcome to Hogwarts.")
