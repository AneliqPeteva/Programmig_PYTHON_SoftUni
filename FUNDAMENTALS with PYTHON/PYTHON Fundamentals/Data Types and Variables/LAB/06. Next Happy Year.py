years = int(input())

while True:
    years += 1
    years_str = str(years)
    if len(set(years_str)) == len(years_str):
        break
print(years)
