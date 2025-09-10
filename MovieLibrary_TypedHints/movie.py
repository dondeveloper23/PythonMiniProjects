from typing import TypedDict

class MovieDict(TypedDict):
    title: str
    year: int
    rating: float

class Movie:
    def __init__(self, data: MovieDict) -> None:
        self.title: str = data["title"]
        self.year: int = data["year"]
        self.rating: float = data["rating"]