import requests
from bs4 import BeautifulSoup

dict_with_data = {}
req = requests.get("https://www.ozone.bg/gaming/igri/ps4/")
soup = BeautifulSoup(req.content, "html.parser")
list_of_games = soup.findAll("div", class_="col-xs-3 five-on-a-row")
for game in list_of_games:
    title = game.find("span", class_="title")
    price = game.findAll("span", class_="price")
    price_element = price[-1].text.strip().replace("\xa0лв.", "")
    if not title.text.replace("(PS4) ", "") in dict_with_data:
        dict_with_data[title.text.replace("(PS4)", "")] = price_element

print(dict_with_data)