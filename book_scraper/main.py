import argparse
from bs4 import BeautifulSoup
import requests
import re

from books import BookCounter, Book

req = requests.get("http://books.toscrape.com/catalogue/category/books_1/page-2.html")
soup = BeautifulSoup(req.content, "html.parser")
content = soup.find_all(class_="current")
pages = content[0].text.split()
max_page = pages[-1]
print(max_page)

books = BookCounter(4)
book_dict = {}



for page in range(2):
    url = "http://books.toscrape.com/catalogue/category/books_1/page-"+str(page)+".html"
    req = requests.get(url)
    soup = BeautifulSoup(req.content, "html.parser")
    content = soup.find_all(class_="product_pod")
    content = str(content)

    pattern_title = r'(?<=title=")(.*?)(?=">)'
    titles_list = re.finditer(pattern_title, content)
    pattern_price = r'(?<=price_color">)(.*?)(?=</p>)'
    price_list = re.finditer(pattern_price, content)
    for title, price in zip(titles_list, price_list):
        # print(f"title {title.group()} = {price.group()}")
     books.add_a_book(Book(title.group(), price.group()))
     if books.if_number_reached():
         books.print_info()




