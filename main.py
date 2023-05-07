import requests
from bs4 import BeautifulSoup

# URL = "https://www.empireonline.com/movies/features/best-movies-2/"

URL = "https://www.timeout.com/film/best-movies-of-all-time"

response = requests.get(URL)
website_html = response.text

soup = BeautifulSoup(website_html, "html.parser")

movie = soup.find_all(name="h3", class_="_h3_cuogz_1")
# print(movie)

movie_titles = [i.getText() for i in movie]
# movies = movie_titles[::-1] # Use this code to reverse the order of the list. (e.g. from 1 to 100 or from 100 to 1)
# print(movie_titles)

for i in movie_titles:
    print(i)

with open("movie.txt", mode="w") as file:
    for i in movie_titles:
        file.write(f"{i}\n")
