from bs4 import BeautifulSoup
import requests
# from Model.index import Articles
from datetime import datetime
import json





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
                {"title": title.text, "article": article.text, "link": link, "date": datetime.today().strftime('%Y-%m-%d')})
    if organization == "WSJ":
        source = requests.get("https://www.wsj.com/news/technology?mod=nav_top_section").text
        soup = BeautifulSoup(source, "html.parser")
        article = soup.findAll("article")
        for list_item in article:
            link = list_item.a["href"]
            title = list_item.a
            if title.text != "":
                dict_.append({"title":title.text, "link":link, "date": datetime.today().strftime('%Y-%m-%d')})
    return dict_


# def save_articles(articles):
#     try:
#         return Articles.insert(title=articles("title"), article=articles("article"), link=articles("link"), date=articles("date")).execute()
#     except:
#         return "Article Already Saved"

def search_for(query):
    nyt_source = requests.get(f"https://www.nytimes.com/search?query={query}").text
    wsj_source = requests.get(f"https://www.wsj.com/search?query={query}&mod=searchresults_viewallresults").text
    nyt_soup = BeautifulSoup(nyt_source, "html.parser")
    wsj_soup = BeautifulSoup(wsj_source, "html.parser")
    # wsj_article = wsj_soup.findAll("article")
    # print(wsj_article)
    # for article in wsj_article:
    #     print(article)
    print(wsj_soup.findAll("article"))

   
#     # return  json.dumps(wsj_soup.decode("utf-8"))



search_for("iphone")

# def get_all_saved_articles():
#     try:
#         data = []
#         for instance in Articles.select():
#             data.append({"id": instance.id, "title": instance.title, "article": instance.article, "link": instance.link, "date": instance.date})
#         return data
#     except:
#         return "No Articles Found"
        
# def get_articles_by_value(value):
#     data = []
#     if value == "NYT" or value == "WSJ":
#         for instance in Articles.select().where(Articles.article == value).get():
#             data.append({"id": instance.id, "title": instance.title, "article": instance.article, "link": instance.link, "date": instance.date})
#         return data       
#     else:
#         print(Articles.select().where(Articles.title == value.replace("-", " ")).get())
#         return True

    