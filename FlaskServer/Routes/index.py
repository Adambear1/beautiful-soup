from bs4 import BeautifulSoup
import requests





def get_articles(organization=None):
    dict_ = []
    if organization == "NYT":
        source = requests.get("https://www.nytimes.com/section/technology").text
        soup = BeautifulSoup(source, "html.parser")
        section = soup.findAll("li", class_="css-ye6x8s")  
        for list_item in section:
            link = list_item.a["href"]
            title = list_item.h2
            article = list_item.p
            dict_.append(
                {"title": title.text, "article": article.text, "link": link})
    if organization == "WSJ":
        source = requests.get("https://www.wsj.com/news/technology?mod=nav_top_section").text
        soup = BeautifulSoup(source, "html.parser")
        article = soup.findAll("article")
        for list_item in article:
            link = list_item.a["href"]
            title = list_item.a
            if title.text != "":
                dict_.append({"title":title.text, "link":link})
    return dict_


