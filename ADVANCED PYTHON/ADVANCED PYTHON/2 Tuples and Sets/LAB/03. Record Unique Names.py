number = int(input())
names_data = {input() for _ in range(number)}

for name in names_data:
    print(name)


# number = int(input())
# names_data = []
# for num in range(number):
#     names_data.append(input())
#
# unique_name = set(names_data)
# for name in unique_name:
#     print(name)


# number = int(input())
# names_data = []
# for num in range(number):
#     name = input()
#     if name not in names_data:
#         names_data.append(name)
#
# for name in names_data:
#     print(name)