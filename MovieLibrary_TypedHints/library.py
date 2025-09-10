from typing import List
from movie import Movie

class Library:
    def __init__(self):
        self.movies: List[Movie] = []

    def add_movie(self, movie: Movie) -> None:
        self.movies.append(movie)

    def get_movie_titles(self) -> List[str]:
        return [movie.title for movie in self.movies]