import requests
from bs4 import BeautifulSoup
import re
import json

req = requests.get("http://books.toscrape.com/catalogue/category/books_1/index.html")

soup = BeautifulSoup(req.content, "html.parser")
# content = soup.find_all(class_="side_categories")
content = soup.findAll(class_="nav nav-list").text
# print(content[0])
data = json.loads(content)
# title_pattern = r'(?<=title=")([M|S](.*?))(?=">)'
# titles_list = re.finditer(title_pattern, content)
# for title in titles_list:
#     if 10 <= len(title.group()) <= 20:
#         print(title.group())


