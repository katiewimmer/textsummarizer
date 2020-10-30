from urllib.request import urlopen
from bs4 import BeautifulSoup

articleURL = "https://www.nytimes.com/2020/04/10/world/canada/coronavirus-canada-detroit-nurses-hospital.html"

def getTextArticle(url):
    page = urlopen(articleURL).read().decode('utf8','ignore')
    soup = BeautifulSoup(page,"lxml")

    # Collecting all articles
    text = ' '.join(map(lambda p: p.text, soup.find_all('article')))

    return text
    
    # Removing funny characters before return
    # return text.encode('ascil', errors = 'replace').replace("?"," ")

# Finding First Article
# soup.find('article').text

print(getTextArticle(articleURL))