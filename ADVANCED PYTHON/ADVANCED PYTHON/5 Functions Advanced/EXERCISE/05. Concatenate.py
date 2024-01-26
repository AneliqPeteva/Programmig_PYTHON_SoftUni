def concatenate(*args, **kwargs):
    text = "".join(args)

    for k, v in kwargs.items():
        text = text.replace(k, v)
    return text



print(concatenate("Soft", "UNI", "Is", "Grate", "!", UNI="Uni", Grate="Great"))
print(concatenate("I", " ", "Love", " ", "Cythons", C="P", s="", java='Java'))
