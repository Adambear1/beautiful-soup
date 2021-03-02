from bs4 import BeautifulSoup
import requests


source = requests.get(
    "https://www.nytimes.com/section/technology").text
soup = BeautifulSoup(source, "html.parser")


def get_articles():
    section = soup.findAll("li", class_="css-ye6x8s")

    dict_ = []
    for list_item in section:
        link = list_item.a["href"]
        title = list_item.h2
        article = list_item.p
        dict_.append(
            {"title": title.text, "article": article.text, "link": link})
    return dict_
