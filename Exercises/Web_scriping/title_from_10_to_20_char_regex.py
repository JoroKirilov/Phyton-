import requests
from bs4 import BeautifulSoup
import re

req = requests.get("http://books.toscrape.com/catalogue/category/books_1/index.html")

soup = BeautifulSoup(req.content, "html.parser")
content = soup.find_all(class_="product_pod")
content = str(content)

title_pattern = r'(?<=title=")[M|S](.){9,19}(?=">)'
titles_list = re.finditer(title_pattern, content)
for title in titles_list:
        print(title.group())