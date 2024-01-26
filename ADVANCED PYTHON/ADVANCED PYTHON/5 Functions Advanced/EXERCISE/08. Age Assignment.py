
def age_assignment(*args, **kwargs):
    result = []
    for letter , age in kwargs.items():
        for name in args:
            if name.startswith(letter):
                result.append(f"{name} is {age} years old.")
                break

    return '\n'.join(sorted(result))

print(age_assignment("Peter", "George", G=26, P=19))