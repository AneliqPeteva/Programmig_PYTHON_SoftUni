w = float(input())
h = float(input())

widht_hall = h * 100 - 100
number_desks_for_row = widht_hall // 70
length_hall = (w * 100)
number_row = length_hall // 120

counts_places = (number_desks_for_row * number_row) - 3

print(int(counts_places))