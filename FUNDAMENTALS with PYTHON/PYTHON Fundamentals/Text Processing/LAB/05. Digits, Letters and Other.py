data = input()
digit = ""
letter = ""
other = ""

for symbol in data:
    if symbol.isdigit():
        digit += symbol
    elif symbol.isalpha():
        letter += symbol
    else:
        other += symbol

print(f"{digit}\n{letter}\n{other}")