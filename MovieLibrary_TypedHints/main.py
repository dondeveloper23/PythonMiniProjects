from movie import Movie, MovieDict
from library import Library

movie1: MovieDict = {"title": "Inception", "year": 2010, "rating": 8.8}
movie2: MovieDict = {"title": "The Matrix", "year": 1999, "rating": 8.7}

m1 = Movie(movie1)
m2 = Movie(movie2)

lib = Library()

lib.add_movie(m1)
lib.add_movie(m2)


print(lib.get_movie_titles())