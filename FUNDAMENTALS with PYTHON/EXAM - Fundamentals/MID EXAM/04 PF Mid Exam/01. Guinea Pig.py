quantity_food_kg = float(input())
quantity_hay_kg = float(input())
quantity_cover_kg = float(input())
guinea_weight_kg = float(input())
days_of_month = 30

for day in range(1, days_of_month +1):
    quantity_food_kg -= 0.300
    if day % 2 == 0:
        quantity_hay_kg -= quantity_food_kg * 0.05
    if day % 3 == 0:
        quantity_cover_kg -= guinea_weight_kg * 1/3
    if quantity_food_kg <= 0 or quantity_hay_kg <= 0 or quantity_cover_kg <= 0:
        print("Merry must go to the pet store!")
        break
else:
    print(f"Everything is fine! Puppy is happy! Food: {quantity_food_kg:.2f}, Hay: {quantity_hay_kg:.2f}, Cover: {quantity_cover_kg:.2f}.")





