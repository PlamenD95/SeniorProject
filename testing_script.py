import feedparser
from urllib import request
from bs4 import BeautifulSoup
import sentiment_mod as sent

f = request.urlopen('https://www.independent.co.uk/news/world/americas/oregon-police-wild-deer-shoot-arrows-shady-cove-portland-hunting-animal-cruelty-a8329511.html')
soup = BeautifulSoup(f, 'html.parser')
print(soup.prettify())