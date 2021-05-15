from bs4 import BeautifulSoup
import requests

url ="https://www.empireonline.com/movies/features/best-movies-2/"

movies_data = requests.get(url)
soup = BeautifulSoup(movies_data.text,
"html.parser")

# print(soup.prettify())

# div_elements = soup.find_all(name="div");

