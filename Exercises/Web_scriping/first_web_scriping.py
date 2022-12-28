import requests
from bs4 import BeautifulSoup
import re

req = requests.get("http://books.toscrape.com/catalogue/category/books_1/index.html")

soup = BeautifulSoup(req.content, "html.parser")
content = soup.find_all(class_="product_pod")
content = str(content)
pattern = r'(?<=title=")([M|S](.*?))(?=">)'
titles_list = re.finditer(pattern, content)
for title in titles_list:
    if 10 <= len(title.group()) <= 20:
        print(title.group())


