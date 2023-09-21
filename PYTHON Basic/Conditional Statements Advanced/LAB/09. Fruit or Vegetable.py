'''
# Read user input
name = input()
type = ""
# Logic
if name == "banana" or name == "apple" or name == "kiwi" or name == "cherry" or name == "lemon" or name == "grapes":
    type = "fruit"
elif name == "tomato" or name == "cucumber" or name == "pepper" or name == "carrot":
    type = "vegetable"
else:
    type = "unknown"

# Print output
print(type)
'''

name = input()
type = "unknown"
# Logic
if name == "banana" or name == "apple" or name == "kiwi" or name == "cherry" or name == "lemon" or name == "grapes":
    type = "fruit"
elif name == "tomato" or name == "cucumber" or name == "pepper" or name == "carrot":
    type = "vegetable"

# Print output
print(type)