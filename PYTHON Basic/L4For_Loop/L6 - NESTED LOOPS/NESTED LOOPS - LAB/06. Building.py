number_floors = int(input())
number_rooms = int(input())

for floors in range(number_floors, 0, -1):
    for rooms in range(number_rooms):
        if floors == number_floors or number_rooms == 1:
            print(f"L{floors}{rooms}", end= " ")
        elif floors % 2 == 0:
            print(f"O{floors}{rooms}", end=" ")
        else:
            print(f"A{floors}{rooms}", end=" ")
    print()