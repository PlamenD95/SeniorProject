import feedparser
import urllib.request
from bs4 import BeautifulSoup

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
        print(post.title + ": " + post.link + "/n")

url = "https://edition.cnn.com/2018/04/27/politics/donald-trump-korea/index.html"
f = urllib.request.urlopen(url)
#print (f.read())
soup = BeautifulSoup(f, 'html.parser')
print(soup.prettify())

