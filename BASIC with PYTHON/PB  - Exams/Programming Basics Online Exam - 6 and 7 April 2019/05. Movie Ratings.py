count_movie = int(input())
max_rating = 0
min_rating = 0
name_film_with_max_rating = ""
name_film_with_min_rating = ""
rating_all_movies = 0

for current_movie in range(1, count_movie + 1):
    name_movie = input()
    rating_movie = float(input())
    rating_all_movies += rating_movie
    if current_movie == 1:
        max_rating = rating_movie
        min_rating = rating_movie
        name_film_with_max_rating = name_movie
        name_film_with_min_rating = name_movie
    if max_rating < rating_movie:
        max_rating = rating_movie
        name_film_with_max_rating = name_movie
    elif min_rating > rating_movie:
        min_rating = rating_movie
        name_film_with_min_rating = name_movie

average = rating_all_movies / count_movie

print(f"{name_film_with_max_rating} is with highest rating: {max_rating:.1f}")
print(f"{name_film_with_min_rating} is with lowest rating: {min_rating:.1f}")
print(f"Average rating: {average:.1f}")
