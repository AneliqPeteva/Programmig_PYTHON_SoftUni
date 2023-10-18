class Movie:
    __watched_movies = []
    def __init__(self, name, director):
        self.name = name
        self.director = director
        self.watched = False

    def change_name(self, new_name):
        self.name = new_name
    def change_director(self, new_director):
        self.director = new_director
    def watch(self):
        if self.watched:
            return

        self.watched = True
        self.__watched_movies.append(self.name)
    def __repr__(self):
        return f"Movie name: {self.name}; Movie director: {self.director}. Total watched movies: {len(self.__watched_movies)}"



