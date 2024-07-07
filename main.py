import requests
from bs4 import BeautifulSoup

url="https://quotes.toscrape.com/"
r= requests.get(url)
# print(r)

soup = BeautifulSoup(r.text,"lxml")
# print(soup)

quotes= soup.find_all("span",class_="text")
for i in quotes:
    print(i.text)


writer=soup.find_all("small",class_="author")
for i in writer:
    print(i.text)
