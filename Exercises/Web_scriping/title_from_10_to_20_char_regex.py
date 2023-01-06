import requests
from bs4 import BeautifulSoup
import re

first_part = "http://books.toscrape.com/catalogue/page-"
second_part = ".html"
for index in range(1, 51):
    searching_url = first_part + str(index) + second_part
    req = requests.get(searching_url)
    soup = BeautifulSoup(req.content, "html.parser")
    content = soup.find_all(class_="product_pod")
    content = str(content)
    title_pattern = r'(?<=title=")[M|S](.){9,19}(?=">)'
    titles_list = re.finditer(title_pattern, content)
    for title in titles_list:
        print(title.group())
