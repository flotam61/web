import requests
from bs4 import BeautifulSoup

KEYWORDS = ['дизайн', 'фото', 'web', 'python']
IDARTICLE = []
urlhabr = "https://habr.com"


# res = requests.get("https://habr.com")
res = requests.get("https://habr.com/ru")
if res.status_code == 200:
    print("Подключение успешно:")

soup = BeautifulSoup(res.text, 'html.parser')
el = soup.find_all("article")

for namearticle in el:
    idart = BeautifulSoup(namearticle['id'], 'html.parser')
    head_art = namearticle.find(class_="tm-article-snippet__title-link")
    head_art_find = head_art.find('span').text
    for key in KEYWORDS:
        if key in head_art_find:
            IDARTICLE.append(idart)

for namehubs in el:
    idart = BeautifulSoup(namehubs['id'], 'html.parser')
    hubs = namehubs.find_all(class_="tm-article-snippet__hubs-item")
    hubs = [hub.find("span").text for hub in hubs]
    for key in KEYWORDS:
        if key in hubs:
            if idart in IDARTICLE:
                print("")
            else:
                IDARTICLE.append(idart)

for text_art in el:
    idart = BeautifulSoup(text_art['id'], 'html.parser')
    text_article = text_art.find_all(class_="article-formatted-body article-formatted-body_version-2")
    text_article = [ta.find("p").text for ta in text_article]
    for key in KEYWORDS:
        for text_article1 in text_article:
            if key in text_article1:
                if idart in IDARTICLE:
                    print("")
                else:
                    IDARTICLE.append(idart)

for x in IDARTICLE:
    # print(x)
    for y in el:
        idart = BeautifulSoup(y['id'], 'html.parser')
        if x == idart:
            m = y.find(class_="tm-article-snippet__title-link")
            m = m.find("span").text
            n = y.find("time").text
            b = y.find(class_="tm-article-snippet__title-link")
            by = b['href']
            print (f"Название: {m}"f". Время: {n}"f". Ссылка: {urlhabr}{by}")