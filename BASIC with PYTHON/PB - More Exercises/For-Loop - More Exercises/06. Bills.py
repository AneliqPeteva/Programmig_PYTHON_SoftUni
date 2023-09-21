# Read user input
mounts = int(input())

water = 20
internet = 15
all_mounts_water = mounts * water
all_mounts_internet = mounts * internet
all_mounts_electricity = 0
all_mounts_other = 0
# Logic
for i in range(mounts):
    electricity = float(input())
    all_mounts_electricity += electricity
    all_mounts_other += water + internet + electricity + (water + internet + electricity) * 0.20

average = (all_mounts_water + all_mounts_internet + all_mounts_electricity + all_mounts_other) / mounts
# Print output
print(f"Electricity: {all_mounts_electricity:.2f} lv")
print(f"Water: {all_mounts_water:.2f} lv")
print(f"Internet: {all_mounts_internet:.2f} lv")
print(f"Other: {all_mounts_other:.2f} lv")
print(f"Average: {average:.2f} lv")