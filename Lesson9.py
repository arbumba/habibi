import requests
from bs4 import BeautifulSoup

url = "https://sinoptik.ua/"
response = requests.get(url)
print(response)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, "html.parser")
    temp = soup.find_all("p", {"class":"R1ENpvZz"})
    for i in temp:
        print(i.text)

"""
import requests
from bs4 import BeautifulSoup

response = requests.get("https://coinmarketcap.com/")
if response.status_code == 200:
    soup = BeautifulSoup(response.text, "html.parser")
    list_1 = soup.find_all("div", {"class":"sc-fa25c04c-0 eAphWs"})
    res = list_1[1].find("span")
    print(res.text)
"""

"""
response = requests.get("https://coinmarketcap.com/")
responext = response.text
responarse = responext.split("<span>")

for element in responarse:
    if element.startswith("$"):
        print(element)
"""

"""
opener = urllib.request.build_opener()
response = opener.open("https://www.python.org/")
print(response.read())

print("-----")

response1 = requests.get("https://www.python.org/")
print(response1.text)
"""
