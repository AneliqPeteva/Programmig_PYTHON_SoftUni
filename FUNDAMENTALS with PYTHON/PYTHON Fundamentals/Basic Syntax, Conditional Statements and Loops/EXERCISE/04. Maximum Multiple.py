'''
divisor = int(input())
boundary = int(input())
number = 0
for i in range(1, boundary + 1):
    if i % divisor == 0:
        number = i

print(f"{number}")
'''


divisor = int(input())
boundary = int(input())

for number in range(boundary, divisor -1, -1):
    if number % divisor == 0:
        break
print(number)