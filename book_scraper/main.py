import argparse
from bs4 import BeautifulSoup
import requests
import re

req = requests.get("http://books.toscrape.com/catalogue/category/books_1/page-2.html")
soup = BeautifulSoup(req.content, "html.parser")
content = soup.find_all(class_="current")
pages = content[0].text.split()
max_page = pages[-1]

book_dict = {}

for page in range(2, int(max_page)):
    url = "http://books.toscrape.com/catalogue/category/books_1/page-"+str(page)+".html"
    req = requests.get(url)
    soup = BeautifulSoup(req.content, "html.parser")
    content = soup.find_all(class_="product_pod")
    content = str(content)

    pattern_title = r"(?<=title=)(.*?)(?=>)"
    titles_list = re.finditer(pattern_title, content)
    pattern_price = r'(?<=price_color">)(.*?)(?=</p>)'
    price_list = re.finditer(pattern_price, content)
    titles = []
    prices = []
    for element in titles_list:
        titles.append(element.group())
    for element in price_list:
        prices.append(element.group())
    for idx in range(len(titles)):
        book_dict[titles[idx]] = prices[idx]

if "book_price":
    print()



if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Welcome to web scraper")
    parser.add_argument("p", dest="book_price", choices=book_dict, nargs="+", help="Book prices")
#     parser.add_argument("-b", dest="genres", choices=GENRES, nargs="+", help="List of genres to search through")
#     parser.add_argument("size", type=str, choices=SIZES.keys(), help='Size of your shirt')
#     parser.add_argument('color', type=str, choices=COLORS.keys(), help="Color or your shirt")
#     parser.add_argument('-l', '--logo', action='store_true', dest='logo', help="add logo to your shirt")
#     parser.add_argument('--soft-fabric', action='store_true', dest='fabric', help='Makes your shirt softer')
#     parser.add_argument('-c', '--custom', type=str, dest='custom', nargs="+", help='Customise your shirt')
#     # parser.add_argument("-g", dest="genres", choices=GENRES, nargs="+", help="List of genres to search through")
#     parsed_args = parser.parse_args()
#     print(make_shirt(parsed_args))