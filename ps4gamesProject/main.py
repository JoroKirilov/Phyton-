import requests
from bs4 import BeautifulSoup


def get_html_content(url):
    """
    this is function that return html content
    param1: url address
    """
    req = requests.get(url)
    return req.content


def get_next_page(soup_content):
    next_page = soup_content.find("a", class_="next")
    return next_page


def sraper():
    dict_with_data = {}
    next_page = "https://www.ozone.bg/gaming/igri/ps4/"
    while next_page != "javascript:;":
        soup = BeautifulSoup(get_html_content(next_page), "html.parser")
        list_of_games = soup.findAll("div", class_="col-xs-3 five-on-a-row")
        for game in list_of_games:
            title = game.find("span", class_="title")
            title = title.text.replace("(PS4)", "")
            price = game.findAll("span", class_="price")
            price_element = price[-1].text.strip().replace("\xa0лв.", "")
            url = game.find("a", class_="product-box")["href"]
            dict_with_data[title] = [price_element, url]
        next_page = str(get_next_page(soup)["href"])

    return dict_with_data

games = dict(sorted(sraper().items(), key=lambda x: x))
with open("data.txt", "w", encoding="utf-8") as file:
    for key, value in games.items():
        file.write(f"{key} - {value[0]} lv --- {value[1]}\n")





