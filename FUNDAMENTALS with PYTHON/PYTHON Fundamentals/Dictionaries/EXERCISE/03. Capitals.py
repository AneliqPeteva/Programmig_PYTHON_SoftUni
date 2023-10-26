# country = input().split(", ")
# capital = input().split(", ")
#
# information = {country[index]: capital[index] for index in range(len(capital))}
# for country, capital in information.items():
#     print(f"{country} -> {capital}")

country = input().split(", ")
capital = input().split(", ")

information = dict(zip(country, capital))
for country, capital in information.items():
    print(f"{country} -> {capital}")