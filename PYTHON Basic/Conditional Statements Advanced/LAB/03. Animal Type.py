# Read user input
animal_type = input()

# Logic
if animal_type == "dog":
    print("mammal")
elif animal_type == "crocodile" or animal_type == "tortoise" or animal_type == "snake":
    print("reptile")
else:
    print("unknown")

# Print output