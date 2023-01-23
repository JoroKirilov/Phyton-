import argparse
from bs4 import BeautifulSoup
import requests

req = requests.get("http://books.toscrape.com/catalogue/category/books_1/index.html")
soup = BeautifulSoup(req.content, "html.parser")
content = soup.find_all(class_="product_pod")
content = str(content)
print(content)





# if __name__ == "__main__":
#     parser = argparse.ArgumentParser(description="Welcome to web scraper")
#     parser.add_argument("-b", dest="genres", choices=GENRES, nargs="+", help="List of genres to search through")
#     parser.add_argument("size", type=str, choices=SIZES.keys(), help='Size of your shirt')
#     parser.add_argument('color', type=str, choices=COLORS.keys(), help="Color or your shirt")
#     parser.add_argument('-l', '--logo', action='store_true', dest='logo', help="add logo to your shirt")
#     parser.add_argument('--soft-fabric', action='store_true', dest='fabric', help='Makes your shirt softer')
#     parser.add_argument('-c', '--custom', type=str, dest='custom', nargs="+", help='Customise your shirt')
#     # parser.add_argument("-g", dest="genres", choices=GENRES, nargs="+", help="List of genres to search through")
#     parsed_args = parser.parse_args()
#     print(make_shirt(parsed_args))