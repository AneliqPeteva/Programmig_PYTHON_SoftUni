with open("text.txt") as file:
    for row, line in enumerate(file):
        if row % 2 == 0:
            for char in "-,.!?":
                line = line.replace(char, "@")
            print(" ".join(reversed(line.split())))