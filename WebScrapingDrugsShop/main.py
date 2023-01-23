from bs4 import BeautifulSoup
import requests
import re

url = "https://www.1mg.com/drugs-all-medicines"
res = requests.get(url)

tmp = str(res.content)
print(tmp)
