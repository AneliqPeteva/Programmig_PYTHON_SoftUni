name_movie = input()
type_hall = input()
count_ticket = int(input())
total_sum = 0
#logic
if name_movie == "A Star Is Born":
    if type_hall == "normal":
        price = 7.50
        total_sum = price * count_ticket
    elif type_hall == "luxury":
        price = 10.50
        total_sum = price * count_ticket
    elif type_hall == "ultra luxury":
        price = 13.50
        total_sum = price * count_ticket
elif name_movie == "Bohemian Rhapsody":
    if type_hall == "normal":
        price = 7.35
        total_sum = price * count_ticket
    elif type_hall == "luxury":
        price = 9.45
        total_sum = price * count_ticket
    elif type_hall == "ultra luxury":
        price = 12.75
        total_sum = price * count_ticket
elif name_movie == "Green Book":
    if type_hall == "normal":
        price = 8.15
        total_sum = price * count_ticket
    elif type_hall == "luxury":
        price = 10.25
        total_sum = price * count_ticket
    elif type_hall == "ultra luxury":
        price = 13.25
        total_sum = price * count_ticket
elif name_movie == "The Favourite":
    if type_hall == "normal":
        price = 8.75
        total_sum = price * count_ticket
    elif type_hall == "luxury":
        price = 11.55
        total_sum = price * count_ticket
    elif type_hall == "ultra luxury":
        price = 13.95
        total_sum = price * count_ticket

#print
print(f"{name_movie} -> {total_sum:.2f} lv.")