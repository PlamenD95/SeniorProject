import feedparser
from urllib import request
from bs4 import BeautifulSoup
import sentiment_mod as sent
import summarization as summar

fs = summar.FrequencySummarizer()

def get_valid_input(prompt):
    while True:
        try:
            inputvalue = str(input(prompt))
        except ValueError:
            print("Sorry, I didn't understand that.")
            continue
        else:
            break
    return inputvalue

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
allheadlines = {}

# List of RSS feeds that we will fetch and combine
newsurls = {
    'CNN': 'http://rss.cnn.com/rss/edition.rss',
    'NY Times': 'http://rss.nytimes.com/services/xml/rss/nyt/HomePage.xml',
    'BBC': 'http://feeds.bbci.co.uk/news/world/rss.xml',
    'The Guardian': 'https://www.theguardian.com/world/rss',
    'Independent': 'http://www.independent.co.uk/news/world/rss'
}

userstring = get_valid_input("Please, enter a topic you wish to search for:")

# Iterate over the feed urls
for url in newsurls.values():
    feed1 = parseRSS(url)

    for post in feed1.entries:
        allheadlines[post.title] = post.link

for key, value in allheadlines.items():
    try:
        f = request.urlopen(value)
        soup = BeautifulSoup(f, 'html.parser')
    except:
        pass

    str = ''

    if 'video' in value:
        continue
    else:
        if 'cnn' in value and userstring in key:
            for div in soup.find_all('div', class_='zn-body__paragraph'):
                str = str + div.text + ' '
            if str == '':
                for par in soup.find_all('p'):
                    str = str + par.text + ' '

        elif 'nytimes' in value and userstring in key:
            for par in soup.find_all('p'):
                str = str + par.text + ' '

        elif 'bbc' in value and userstring in key:
            for par in soup.find_all('p'):
                str = str + par.text + ' '

        elif 'theguardian' in value and userstring in key:
            for par in soup.find_all('p'):
                str = str + par.text + ' '

        elif 'independent' in value and userstring in key:
            for par in soup.find_all('p'):
                str = str + par.text + ' '

        else:
            print("The topic of your choice is not present in the '%s' article.\n" % key)
            print("-----------------------------------------")
            continue

        print(key, value)
        for sumstr in fs.summarize(str, 4):
            print('*', sumstr)
        print(sent.sentiment(str))
        print("-----------------------------------------")