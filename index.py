from bs4 import BeautifulSoup
import requests

source = requests.get(
    "https://www.nytimes.com/section/technology").text
soup = BeautifulSoup(source, "html.parser")
a_tags = soup.findAll(
    "a")

titles = []
for title in a_tags:
    if title["href"]:
        titles.append(title["href"])


print(titles)
