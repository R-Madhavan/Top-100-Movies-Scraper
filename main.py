import requests
from bs4 import BeautifulSoup

# Fetch the webpage
response = requests.get("https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/")
top_100_movies_webpage = response.text

# Parse the webpage
movies_list = []
soup = BeautifulSoup(top_100_movies_webpage, "html.parser")
movie_title_tags = soup.find_all(name="h3", class_="title")

# Extract movie titles
for movies_tags in movie_title_tags:
    movies = movies_tags.get_text()
    movies_list.append(movies)

# Reverse the list
reverse_movie_list = movies_list[::-1]

# Fix encoding issues in the movie titles
fixed_movie_list = [movie.encode('latin1').decode('utf-8') for movie in reverse_movie_list]

# Print the reversed and fixed list
print(fixed_movie_list)

# Write fixed titles to the file
with open("movies.txt", "w", encoding="utf-8") as file:
    for movie in fixed_movie_list:
        file.write(f"{movie}\n")
