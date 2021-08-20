from bs4 import BeautifulSoup
import requests
import colorama
from googletrans import Translator
######################################

HEADERS = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:91.0) Gecko/20100101 Firefox/91.0'
}

translator = Translator()

#####################################
print(colorama.Style.BRIGHT + colorama.Back.BLACK + colorama.Fore.YELLOW + "******************************")
# CBC
print("CBC:")
url_cbc = "https://www.cbc.ca/news/world"

request = requests.get(url_cbc, headers=HEADERS)

soup_cbc = BeautifulSoup(request.text, "html.parser")

header_cbc = soup_cbc.find_all("div", class_="card")

for description_cbc in header_cbc:
    description_cbc = description_cbc.find("a", {'class': 'contentWrapper'})

    if description_cbc is not None:
        link_cbc = description_cbc.get('href')
        original = description_cbc.text
        russian = translator.translate(original, dest='ru')
        print(colorama.Style.BRIGHT + colorama.Back.BLACK + colorama.Fore.CYAN + str(russian.text) + " \n" + (
            str("https://www.cbc.ca" + link_cbc)))
        print(colorama.Style.BRIGHT + colorama.Back.BLACK + colorama.Fore.YELLOW + "******************************")

# NYT
print("The New York Times:")
url_nyt = "https://www.nytimes.com/section/world"

request = requests.get(url_nyt, headers=HEADERS)

soup_nyt = BeautifulSoup(request.text, "html.parser")

header_nyt = soup_nyt.find_all("li", class_="css-ye6x8s")


for description_nyt in header_nyt:
    description_nyt = description_nyt.find("div", {'class': 'css-1l4spti'}).find('a')

    if description_nyt is not None:
        link_nyt = description_nyt.get('href')
        original = description_nyt.text
        russian = translator.translate(original, dest='ru')
        print(colorama.Style.BRIGHT + colorama.Back.BLACK + colorama.Fore.CYAN + str(russian.text) + " \n" + (
            str("https://www.nytimes.com/" + link_nyt)))
        print(colorama.Style.BRIGHT + colorama.Back.BLACK + colorama.Fore.YELLOW + "******************************")

# Aljazeera
print("Aljazeera:")
url_alj = "https://www.aljazeera.com/europe/"
request = requests.get(url_alj, headers=HEADERS)

soup_alj = BeautifulSoup(request.text, "html.parser")

header_alj = soup_alj.find_all("article", class_="gc")

for description_alj in header_alj:
    description_alj = description_alj.find("div", {'class': 'gc__header-wrap'}).find('a')

    if description_alj is not None:
        link_alj = description_alj.get('href')
        original = description_alj.text
        russian = translator.translate(original, dest='ru')
        print(colorama.Style.BRIGHT + colorama.Back.BLACK + colorama.Fore.CYAN + str(russian.text) + " \n" + (
            str("https://www.aljazeera.com" + link_alj)))
        print(colorama.Style.BRIGHT + colorama.Back.BLACK + colorama.Fore.YELLOW + "******************************")

# BBC
print("BBC:")
url_bbc = "https://www.bbc.com/news/world"
request = requests.get(url_bbc, headers=HEADERS)

soup_bbc = BeautifulSoup(request.text, "html.parser")

header_bbc = soup_bbc.find_all("div", {'class': 'gel-wrap'})

for description_bbc in header_bbc:
    description_bbc = description_bbc.find("a", {'class': 'gs-c-promo-heading'})

    if description_bbc is not None:
        link_bbc = description_bbc.get('href')
        original = description_bbc.text
        russian = translator.translate(original, dest='ru')
        print(colorama.Style.BRIGHT + colorama.Back.BLACK + colorama.Fore.CYAN + str(russian.text) + " \n" + (
            str("https://www.bbc.com" + link_bbc)))
        print(colorama.Style.BRIGHT + colorama.Back.BLACK + colorama.Fore.YELLOW + "******************************")
