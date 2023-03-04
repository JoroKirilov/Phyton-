import requests
from bs4 import BeautifulSoup


def get_html_content(url):
    """
    this is function that return html content
    param1: url address
    """
    req = requests.get(url)
    return req.content


dict_with_data = {}
soup = BeautifulSoup(get_html_content("https://www.ozone.bg/gaming/igri/ps4/"), "html.parser")
list_of_games = soup.findAll("div", class_="col-xs-3 five-on-a-row")
for game in list_of_games:
    title = game.find("span", class_="title")
    price = game.findAll("span", class_="price")
    price_element = price[-1].text.strip().replace("\xa0лв.", "")
    if not title.text.replace("(PS4) ", "") in dict_with_data:
        dict_with_data[title.text.replace("(PS4)", "")] = price_element

for key, value in dict_with_data.items():
    print(f"{key} - {value} lv")