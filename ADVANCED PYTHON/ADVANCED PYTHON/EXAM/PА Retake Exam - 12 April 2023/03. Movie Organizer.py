def movie_organizer(*args):
    dictionary, dictionary_length, output = {}, {}, []

    for movie, genre in args:
        dictionary[genre] = dictionary.get(genre, []) + [movie]
        dictionary_length[genre] = dictionary_length.get(genre, 0) + 1

    sorted_dict_genres = sorted(dictionary_length.items(), key=lambda x: (-x[1], x[0]))

    for curr_genre, number in sorted_dict_genres:
        output.append(f"{curr_genre} - {number}")
        sorted_movies = list(sorted(dictionary[curr_genre]))
        for c_movie in sorted_movies:
            output.append(f"* {c_movie}")

    return "\n".join(output)


print(movie_organizer(
    ("The Matrix", "Sci-fi")))

print(movie_organizer(
    ("The Godfather", "Drama"),
    ("The Hangover", "Comedy"),
    ("The Shawshank Redemption", "Drama"),
    ("The Pursuit of Happiness", "Drama"),
    ("The Hangover Part II", "Comedy")))

print(movie_organizer(
    ("Avatar: The Way of Water", "Action"),
    ("House Of Gucci", "Drama"),
    ("Top Gun", "Action"),
    ("Ted", "Comedy"),
    ("Duck Soup", "Comedy"),
    ("The Dark Knight", "Action"),
    ("A Star Is Born", "Musicals"),
    ("The Warrior", "Action"),
    ("Like A Boss", "Comedy"),
    ("The Green Mile", "Drama"),
    ("21 Jump Street", "Comedy")))
