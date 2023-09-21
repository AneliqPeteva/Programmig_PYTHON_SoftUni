# Read user input
search_book = input()
count_book = 0
# Logic
while True:
    user_input = input()
    if user_input == search_book:
        print(f"You checked {count_book} books and found it.")
        break
    elif user_input == "No More Books":
        print(f"The book you search is not here!")
        print(f"You checked {count_book} books.")
        break
    else:
        count_book += 1


# Print output