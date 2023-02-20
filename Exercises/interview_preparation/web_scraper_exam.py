from bs4 import BeautifulSoup
import requests
#
# req = requests.get("https://books.toscrape.com/index.html")
# soup = BeautifulSoup(req.content, 'html.parser')
# category_sidebar = soup.find(class_='nav nav-list')
# category_list = category_sidebar.find_all("a")
# category_dict = {}
# for el in category_list:
#     url = "http://books.toscrape.com/" + el["href"]
#     category_dict[el.text.strip()] = url
#
# print(category_dict)

# url = 'http://books.toscrape.com/catalogue/category/books/travel_2/'
# url = "/".join(url.split("/")[0:-3:1])
# print(url)
# # base_url = "/".join(url.split("/")[0:-3:1])
# # print(base_url)
import requests

req = requests.get("http://books.toscrape.com/catalogue/category/books/sequential-art_5/index.html")
soup = BeautifulSoup(req.content, "html.parser")
books = soup.find_all(class_='col-xs-6 col-sm-4 col-md-3 col-lg-3')
for book in books:
    print(book)