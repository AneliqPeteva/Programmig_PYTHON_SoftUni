import re
n = int(input())
pattern = r"@#+[A-Z][A-Za-z0-9]{4,}[A-Z]@#+"
for string in range(n):
    different_string = input()
    match = re.findall(pattern, different_string)
    if match:
        digit = ""
        for current_element in match[0]:
            if current_element.isdigit():
                digit += current_element
        if digit == "":
            print("Product group: 00")
        else:
            print(f"Product group: {digit}")
    else:
        print("Invalid barcode")




