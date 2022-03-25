import sys
import random

class MovieLibrary:
    def __init__(self, title, year, genre):
        self.title = title
        self.year = year
        self.genre = genre

        # Variables
        self.played = 0

    def play(self, step=1):
        self.played += step
        writing = self.title, self.year
        print(writing)

    def __str__(self):
        return f'{self.title} {self.year} {self.genre}'

    def display(self):
        print(self.title, self.year, self.genre)

    def get_series(self):
        pass

    def get_movies(self):
        if MovieLibrary:
            print(self.title, self.year, self.genre)
        else:
            print("No movie on list")


library = []

Heat = MovieLibrary(title='Heat', year=2000, genre='drama')
Godfather = MovieLibrary(title='The Godfather', year=1972, genre='drama')
Killer = MovieLibrary(title='Killer', year=1999, genre='comedy')
Diuna = MovieLibrary(title='Diuna', year=1976, genre='fantasy')
library.append(Heat)
library.append(Godfather)
library.append(Killer)
library.append(Diuna)

Godfather.play()
Heat.play()
Heat.play()

print(Godfather.played)
print(Heat.played)

print(Heat)


class SeriesLibrary:
    def __init__(self, title, year, genre, number, season):
        self.title = title
        self.year = year
        self.genre = genre
        self.number = number
        self.season = season

        # Variables
        self.played = 0

    def play(self, step=1):
        self.played += step
        writing = self.title, self.year, f'"S%(#)02dE%(t)02d"' % {"#": self.season, "t": self.number}
        print(writing)

    def display(self):
        print(self.title, self.year, self.genre, self.season, self.number)

    def get_series(self):
        if SeriesLibrary:
            print(self.title, self.year, self.genre, self.season, self.number)
        else:
            print("No series on list")

    def get_movies(self):
        pass


Friends = SeriesLibrary(title='Friends', year=2000, genre='sitcom', number=8, season=2)
Blaclist = SeriesLibrary(title='Blacklist', year=2018, genre='drama', number=3, season=4)

library.append(Friends)
library.append(Blaclist)

Friends.play()
Heat.play()

print("")


for i in library:
    i.get_series()
print("")


def search(title, library):
    for movie in library:
        if title in movie.title:
            print(movie)


print("")

for i in library:
    i.get_movies()

print("")

print(search("Heat", library))


def generate_views():
    n = len(library)
    a = random.randint(0,n-1)
    library[a].play()


