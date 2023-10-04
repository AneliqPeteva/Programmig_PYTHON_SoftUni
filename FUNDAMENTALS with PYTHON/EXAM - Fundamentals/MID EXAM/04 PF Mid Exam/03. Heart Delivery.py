neighborhood = [int(x) for x in input().split("@")]
jump_data = input()
neighborhood_len = len(neighborhood)
house_index = 0

while jump_data != "Love!":
    jump, length = jump_data.split()
    house_index += int(length)
    if house_index > neighborhood_len - 1:
        house_index = 0
    if neighborhood[house_index] >= 2:
        neighborhood[house_index] -= 2
        if neighborhood[house_index] == 0:
            print(f"Place {house_index} has Valentine's day.")
    else:
        if neighborhood[house_index] == 0:
            print(f"Place {house_index} already had Valentine's day.")
    jump_data = input()

print(f"Cupid's last position was {house_index}.")
count_house = neighborhood.count(0)
if count_house == neighborhood_len:
    print("Mission was successful.")
else:
    print(f"Cupid has failed {neighborhood_len - count_house} places.")


