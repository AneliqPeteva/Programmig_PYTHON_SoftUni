def sort_names():
    name = input().split(", ")

    return sorted(name, key=lambda x: (-len(x), x))

print(sort_names())
