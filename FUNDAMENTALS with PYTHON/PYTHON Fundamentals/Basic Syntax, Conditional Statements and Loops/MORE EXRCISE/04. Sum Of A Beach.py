string = input().lower()


sand_count = string.count("sand")
water_count = string.count("water")
fish_count = string.count("fish")
sun_count = string.count("sun")

total_count = sand_count + water_count + fish_count + sun_count
print(total_count)