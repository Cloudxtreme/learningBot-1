from bs4 import BeautifulSoup
import requests
from lxml import html

page = requests.get('http://www.randomfunfacts.com/')
tree = (page.content)
soup = BeautifulSoup(tree, 'html.parser')
soup.find_all("i")[0].string
