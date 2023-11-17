import re

destination = input()
travel_points = 0
pattern = r"=[A-Z][A-Za-z][A-Za-z]+=|\/[A-Z][A-Za-z][A-Za-z]+\/"
list_results = []
matches = re.findall(pattern, destination)

for match in matches:
    match = match[1:-1]
    list_results.append(match)
    travel_points += len(match)

print(f'Destinations: {", ".join(list_results)}')
print(f"Travel Points: {travel_points}")

# import re
#
# destination = input()
# travel_points = 0
# pattern = r"([=/])([A-Z][a-zA-Z][a-zA-Z]+)\1"
# list_results = []
# matches = re.finditer(pattern, destination)
# for match in matches:
#     list_results.append(match.group(2))
#     travel_points += len(list_results[-1])
#
# print(f'Destinations: {", ".join(list_results)}')
# print(f"Travel Points: {travel_points}")
