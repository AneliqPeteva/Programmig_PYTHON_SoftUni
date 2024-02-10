import os

while True:
    command, *info = input().split("-")  # Replace-text.txt-a-b -> [text.txt, a, b]

    if command == "Create":
        with open(f"{info[0]}", "w"): pass

    elif command == "Add":
        with open(f"{info[0]}", "a") as file:
            file.write(f"{info[1]}\n")

    elif command == "Replace":
        try:
            with open(f"{info[0]}", "r+") as file:
                text = file.read()
                text = text.replace(info[1], info[2])

                file.seek(0)
                file.write(text)
                file.truncate()

        except FileNotFoundError:
            print(f"An error occurred!")

    elif command == "Delet": # оставено е така, за да се види какво се случва в файла!!! Трябва да е elif command == "Delete":
        try:
            os.remove(f"{info[0]}")
        except FileNotFoundError:
            print(f"An error occurred!")

    elif command == "End":
        break