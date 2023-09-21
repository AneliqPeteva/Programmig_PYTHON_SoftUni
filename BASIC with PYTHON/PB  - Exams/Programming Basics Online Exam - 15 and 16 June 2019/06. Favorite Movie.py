import string
name_movie = input()
count_movie = 0
best_point = 0
best_movie = ""
lower_letters = string.ascii_lowercase
upper_letters = string.ascii_uppercase

while True:
    current_score = 0
    if name_movie == "STOP":
        print(f"The best movie for you is {best_movie} with {best_point} ASCII sum.")
        break

    else:
        for letter in name_movie:

            if letter in lower_letters:
                current_score = current_score + ord(letter) - (len(name_movie) * 2)
            elif letter in upper_letters:
                current_score = current_score + ord(letter) - (len(name_movie))
            else:
                current_score += ord(letter)
        if current_score > best_point:
            best_point = current_score
            best_movie = name_movie


        count_movie += 1
        if count_movie == 7:
            print(f"The limit is reached.\nThe best movie for you is {best_movie} with {best_point} ASCII sum.")
            break

        name_movie = input()