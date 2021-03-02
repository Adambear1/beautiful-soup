from bs4 import BeautifulSoup
import requests

with open('index.html') as html_file:
    soup = BeautifulSoup(html_file, 'html.parser')
    # prints entire document
    soup.prettify()

# Find specific element tag & gets text value
title = soup.title.text
# Find div with specific class name
match = soup.find("div", class_="footer").prettify()
match1 = soup.find("div", class_="article")
# Find navigate through designated string to find specific text
# Class Article -> h2 -> a -> textContent
headline = match1.h2.a.text

# Find All -- Loop through specific tags
for div in soup.find_all("div", class_="article"):
    # Able to pinpoint and grab all texts from specific div/class element
    headline = div.h2.a.text
    summary = div.p.text
