key = int(input())
number = int(input())

for letter in range(number):
    current_letter = input()
    new_letter = ord(current_letter) + key
    print(chr(new_letter), end= "")