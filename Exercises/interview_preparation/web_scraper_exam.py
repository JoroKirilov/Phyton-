from bs4 import BeautifulSoup
import requests

req = requests.get("https://books.toscrape.com/index.html")
soup = BeautifulSoup(req.content, 'html.parser')
category_sidebar = soup.find(class_='nav nav-list')
category_list = category_sidebar.find_all("a")
category_dict = {}
for el in category_list:
    url = "http://books.toscrape.com/" + el["href"]
    category_dict[el.text.strip()] = url

print(category_dict)
