from bs4 import BeautifulSoup
import requests
import re

def add_to_dict(medic):
    temp_dict = {}
    for el in medic:
        data_element = el.text
        name_medicine = data_element.split("MRP")
        temp_dict[name_medicine[0]] = name_medicine[1]
    return temp_dict

drugs = {}

url = "https://www.1mg.com/drugs-all-medicines"
headers = {
    "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.64 Safari/537.36 Edg/101.0.1210.47"
}
res = requests.get(url, headers=headers)
soup = BeautifulSoup(res.content, "html.parser")
max_page = soup.findAll(class_="button-text link-page")
for page in range(2, int(max_page[-1].text) + 1):
    url = "https://www.1mg.com/drugs-all-medicines?page="+str(page)
    req = requests.get(url, headers=headers)
    soup = BeautifulSoup(req.content, "html.parser")
    medicine = soup.findAll(class_="style__font-bold___1k9Dl style__font-14px___YZZrf style__flex-row___2AKyf style__space-between___2mbvn style__padding-bottom-5px___2NrDR")
    drugs.update(add_to_dict(medicine))

print(drugs)



# https://www.1mg.com/drugs-all-medicines?page=2
medic = soup.findAll(class_="style__font-bold___1k9Dl style__font-14px___YZZrf style__flex-row___2AKyf style__space-between___2mbvn style__padding-bottom-5px___2NrDR")

print(drugs["Augmentin 625 Duo Tablet"])

print(chr(97))

# https://www.1mg.com/drugs-all-medicines?page=2&label=b