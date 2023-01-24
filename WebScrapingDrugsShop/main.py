from bs4 import BeautifulSoup
import requests
import re

url = "https://www.1mg.com/drugs-all-medicines"
headers = {
    "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.64 Safari/537.36 Edg/101.0.1210.47"
}
res = requests.get(url, headers=headers)

soup = BeautifulSoup(res.content, "html.parser")
drugs = {}
medic = soup.findAll(class_="style__font-bold___1k9Dl style__font-14px___YZZrf style__flex-row___2AKyf style__space-between___2mbvn style__padding-bottom-5px___2NrDR")
for el in medic:
    data_element = el.text
    name_medicine = data_element.split("MRP")
    drugs[name_medicine[0]] = name_medicine[1]
print(drugs["Augmentin 625 Duo Tablet"])
page = soup.findAll(class_="button-text link-page")
print(page[-1].text)