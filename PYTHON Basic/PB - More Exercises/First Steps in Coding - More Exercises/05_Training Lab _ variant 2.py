from math import floor
w = float(input())
h = float(input())

area_hall = (int((w * 100) * (h * 100)))
area_desk = floor(70 * 120)
corridor = floor(100 * (w * 100))
counts_places = floor((area_hall - corridor) // area_desk) - 3

print(int(counts_places))
