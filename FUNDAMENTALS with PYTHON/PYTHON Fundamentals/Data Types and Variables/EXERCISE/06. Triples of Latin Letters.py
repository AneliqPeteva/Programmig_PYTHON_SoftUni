number = int(input())

for i in range(number):
    for j in range(number):
        for k in range(number):
            print(f"{chr(97 + i)}{chr(97 + j)}{chr(97 + k)}")