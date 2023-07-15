from bs4 import BeautifulSoup
import requests

# get the website html
response = requests.get(
    "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/")
soup = BeautifulSoup(response.text, "html.parser")

movies = soup.find_all(name="h3", class_="title")

f = 0
moviesList = []

for m in movies:
    moviesList.append(m.get_text())

# slice operator
moviesToBePrint = moviesList[::-1]

with open("bestFilms.txt", "w") as moviesFile:
    for m in moviesToBePrint:
        moviesFile.write(m+"\n")
