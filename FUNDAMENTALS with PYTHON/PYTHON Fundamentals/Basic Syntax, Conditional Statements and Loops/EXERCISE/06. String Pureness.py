n = int(input())

for j in range(n):
    input_text = input()

    length_text = len(input_text)
    for i in range(length_text):
        char = input_text[i]

        if char == "," or char == "." or char == "_":
            print(f"{input_text} is not pure!")
            break
    else:
        print(f"{input_text} is pure.")

