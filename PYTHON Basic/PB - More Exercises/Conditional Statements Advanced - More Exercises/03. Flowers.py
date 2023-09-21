# Read user input
count_chrysanthemums = int(input())
count_roses = int(input())
count_tulips = int(input())
season = input()
feast_day = input()
price_chrysanthemums = 0
price_roses = 0
price_tulips = 0
total_sum = 0
all_count_flowers = count_roses + count_tulips + count_chrysanthemums

# Logic
if season == "Spring" or season == "Summer":
    price_chrysanthemums = count_chrysanthemums * 2.00
    price_roses = count_roses * 4.10
    price_tulips = count_tulips * 2.50
elif season == "Autumn" or season == "Winter":
    price_chrysanthemums = count_chrysanthemums * 3.75
    price_roses = count_roses * 4.50
    price_tulips = count_tulips * 4.15

total_sum = price_tulips + price_roses + price_chrysanthemums

if feast_day == "Y":
    total_sum *= 1.15
if count_tulips > 7 and season == "Spring":
    total_sum *= 0.95
if count_roses >= 10 and season == "Winter":
    total_sum *= 0.90
if all_count_flowers > 20:
    total_sum *= 0.80

total_sum += 2
# Print output
print(f"{total_sum:.2f}")