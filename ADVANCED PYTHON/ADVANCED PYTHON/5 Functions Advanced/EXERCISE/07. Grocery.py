def grocery_store(**kwargs):
    kwargs = sorted(kwargs.items(), key=lambda x: (-x[1], -len(x[0]), x[0]))
    # -x[1] ще сортира от по-голямот, към по-малкото число в тюпъла,
    # след това сортираме с -len(x[0], за да сортира ключа по дължина - от по-дълга към по-къса
    # и накрая x[0], за да се сортира по азбучен ред
    result = []

    for product, quantity in kwargs:
        result.append(f"{product}: {quantity}")

    return '\n'.join(result)


print(grocery_store(
    bread=5,
    pasta=12,
    eggs=12,
))
print(grocery_store(
    bread=2,
    pasta=2,
    eggs=20,
    carrot=1,
))
