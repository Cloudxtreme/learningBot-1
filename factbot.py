from bs4 import BeautifulSoup
import requests
from lxml import html

def scrapeFacts():
    page = requests.get('http://www.randomfunfacts.com/')
    tree = (page.content)
    soup = BeautifulSoup(tree, 'html.parser')
    fact = soup.find_all("i")[0].string
    print(fact)


scrapeFacts()
