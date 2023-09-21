numbers = int(input())
bonus = 0

if numbers <= 100:
    bonus = 5
elif numbers > 1000:
    bonus = numbers * 0.1
else:
    bonus = numbers * 0.2

if numbers % 2 == 0:
    bonus += 1
elif numbers % 10 == 5:
    bonus += 2

print(bonus)
print(bonus + numbers)