import feedparser
from urllib import request
from bs4 import BeautifulSoup
import sentiment_mod as sent

# Function to fetch the rss feed and return the parsed RSS
def parseRSS(rss_url):
    return feedparser.parse(rss_url)

# Function grabs the rss feed headlines (titles) and returns them as a list
def getHeadlines(rss_url):
    headlines = []

    feed = parseRSS(rss_url)
    for newsitem in feed['items']:
        headlines.append(newsitem['title'])

    return headlines

# A list to hold all headlines
allheadlines = []

# List of RSS feeds that we will fetch and combine
newsurls = {
    'CNN': 'http://rss.cnn.com/rss/edition.rss'
}

# Iterate over the feed urls
for key, url in newsurls.items():
    # Call getHeadlines() and combine the returned headlines with allheadlines
    allheadlines.extend(getHeadlines(url))

# Iterate over the allheadlines list and print each headline
# for hl in allheadlines:
#     print(hl)

feed1 = parseRSS('http://rss.cnn.com/rss/edition.rss')

for post in feed1.entries:
    print(post.title + ": " + post.link + "\n")

print("-----------------------------------------")

for post in feed1.entries:
    if('Trump' in post.title):
        print(post.title + ": " + post.link + "\n")

        url = post.link
        f = request.urlopen(url)
        soup = BeautifulSoup(f, 'html.parser')

        s = ''
        for div in soup.find_all('div', class_='zn-body__paragraph'):
            s = s + div.text + ' '

        print(s)

        print(sent.sentiment(s))

        print("-----------------------------------------")


feed2 = parseRSS('http://rss.nytimes.com/services/xml/rss/nyt/HomePage.xml')
for post in feed2.entries:
    print(post.title + ": " + post.link + "\n")


f1 = request.urlopen('https://www.nytimes.com/2018/04/29/us/politics/ohio-governor-richard-cordray-dennis-kucinich.html')
soup1 = BeautifulSoup(f1, 'html.parser')

print("-----------------------------------------")

s1 = ''
for par in soup1.find_all('p'):
    s1 = s1 + par.text + ' '

print(s1)

print(sent.sentiment(s1))

print("-----------------------------------------")