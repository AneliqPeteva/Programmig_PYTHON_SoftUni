import string
start_sector = "A"
end_sector = input()

count_row_in_first_sector = int(input())
count_place_odd_row = int(input())
count_all_place = 0



for sector in range(ord("A"), ord(end_sector) + 1):
    if sector == ord("A"):
        count_row_in_first_sector += 0
    else:
        count_row_in_first_sector += 1

    for row in range(1, count_row_in_first_sector + 1):
        count_place_odd_row_new = 0
        if row % 2 != 0:
            count_place_odd_row_new += count_place_odd_row
        else:
            count_place_odd_row_new += count_place_odd_row + 2

        for place in range(ord("a"), ord("a") + count_place_odd_row_new):
            if row % 2 != 0:
                print(f"{chr(sector)}{row}{chr(place)}")
            else:
                print(f"{chr(sector)}{row}{chr(place)}")
            count_all_place += 1

print(count_all_place)





