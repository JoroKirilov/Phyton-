import requests
from bs4 import BeautifulSoup
from collections import defaultdict
import pandas as pd

url = "https://www.1mg.com/drugs-all-medicines"
# res = requests.get(url)
# text = (str(res.content))
# if "Augmentin 625 Duo Tablet" in text:
#     print("True")

headers = {
    'user-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:47.0) Gecko/20100101 Firefox/47.3'}

response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.content, "html.parser")


class1 = "style__font-bold___1k9Dl style__font-14px___YZZrf style__flex-row___2AKyf style__space-between___2mbvn style__padding-bottom-5px___2NrDR"
medic = soup.findAll(class_=class1)

data = {}
for med in medic:
    med_text = med.text
    list1 = med_text.split("MRP₹")
    data[list1[0]] = list1[1]

for key, value in data.items():
    print(key)
    print(value)



