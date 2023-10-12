numbers = input().split(", ")

positive_numbers = [number for number in numbers if int(number) >= 0]
negative_numbers = [number for number in numbers if int(number) < 0]
even_numbers = [number for number in numbers if int(number) % 2 == 0]
odd_numbers = [number for number in numbers if int(number) % 2 != 0]

print(f"Positive: {', '.join(positive_numbers)}")
print(f"Negative: {', '.join(negative_numbers)}")
print(f"Even: {', '.join(even_numbers)}")
print(f"Odd: {', '.join(odd_numbers)}")
