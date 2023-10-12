name = input().split(", ")

sort_name = sorted(name, key=lambda x: (-len(x), x))

print(sort_name)
