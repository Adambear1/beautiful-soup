from bs4 import BeautifulSoup
import requests
# Returns entire html for website, without '.text' it would
# just return status of website
source = requests.get("http://coreyms.com").text
# Entire article parsed + able to read
soup = BeautifulSoup(source, "html.parser")
# Able to get article tag from website
article = soup.find('article')
# Within article div, we find the entry-content class & retrieve info
summary = article.find('div', class_="entry-content").p.text
# Able to get attributes through accessing like a dictionary
vid_src = article.find('iframe', class_="youtube-player")["src"]
# Able to dissect the string through split method, which turns into array
# and able to identify and select correct q-param from there
vid_id_params = vid_src.split("/")
vid_id = vid_id_params[4].split("?")[0]
# Able to reverse engineer + add id back to yt string
yt_link = f'https://youtube.com/watch?v={vid_id}'
