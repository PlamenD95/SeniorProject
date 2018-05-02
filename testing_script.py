import feedparser
from urllib import request
from bs4 import BeautifulSoup
import sentiment_mod as sent

f = request.urlopen('http://money.cnn.com/2018/05/01/media/national-enquirer-president-trump/index.html')
soup = BeautifulSoup(f, 'html.parser')
print(soup.prettify())