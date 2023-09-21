# Read user input
stadium = int(input())
count_all_fans = int(input())
count_sector_a = 0
count_sector_b = 0
count_sector_v = 0
count_sector_g = 0
# Logic
for i in range(count_all_fans):
    sector = input()
    if sector == "A":
        count_sector_a += 1
    elif sector == "B":
        count_sector_b += 1
    elif sector == "V":
        count_sector_v += 1
    elif sector == "G":
        count_sector_g += 1
percent_sector_a = count_sector_a / count_all_fans * 100
percent_sector_b = count_sector_b / count_all_fans * 100
percent_sector_v = count_sector_v / count_all_fans * 100
percent_sector_g = count_sector_g / count_all_fans * 100
all_percent = (count_sector_a + count_sector_b + count_sector_v + count_sector_g) / stadium * 100

# Print output
print(f"{percent_sector_a:.2f}%")
print(f"{percent_sector_b:.2f}%")
print(f"{percent_sector_v:.2f}%")
print(f"{percent_sector_g:.2f}%")
print(f"{all_percent:.2f}%")
