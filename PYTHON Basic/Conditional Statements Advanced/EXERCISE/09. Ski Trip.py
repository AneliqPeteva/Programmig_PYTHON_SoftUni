# Read user input
'''''
	"room for one person" – 18.00 лв за нощувка
	"apartment" – 25.00 лв за нощувка 
	"president apartment" – 35.00 лв за нощувка
Според броят на дните, в които ще остане в хотела (пример: 11 дни = 10 нощувки) и видът на помещението, което ще избере, той може да ползва различно намаление. 
'''''
days_to_stay = int(input())
type_room = input()
rating = input()
price_room_for_one_person = 18.00
price_apartment = 25
price_president_apartment = 35
night_to_stay = days_to_stay - 1
total_sum = 0
# Logic
if type_room == "room for one person":
    total_sum = night_to_stay * price_room_for_one_person
elif type_room == "apartment":
    total_sum = night_to_stay * price_apartment
    if days_to_stay < 10:
        total_sum *= 0.70
    elif days_to_stay > 15:
        total_sum *= 0.50
    else:
        total_sum *= 0.65
elif type_room == "president apartment":
    total_sum = night_to_stay * price_president_apartment
    if days_to_stay < 10:
        total_sum *= 0.90
    elif days_to_stay > 15:
        total_sum *= 0.80
    else:
        total_sum *= 0.85

if rating == "positive":
    total_sum *= 1.25
elif rating == "negative":
    total_sum *= 0.90

# Print output
print(f"{total_sum:.2f}")