from urllib.request import urlopen
from bs4 import BeautifulSoup
import nlbasics
from pprint import pprint
import ssl

try:
    _create_unverified_https_context = ssl._create_unverified_context
except AttributeError:
    pass
else:
    ssl._create_default_https_context = _create_unverified_https_context

# Tokenizing
from nltk.tokenize import word_tokenize, sent_tokenize
# Stopwords
from nltk.corpus import stopwords
from string import punctuation
# Bigrams
from nltk.collocations import *
# Stemming
from nltk.stem.lancaster import LancasterStemmer
# Disambiguation
from nltk.corpus import wordnet as wn
from nltk.wsd import lesk
# Frequency Distribution
from nltk.probability import FreqDist
from heapq import nlargest
from collections import defaultdict

def getTextArticle(url):
    page = urlopen(articleURL).read().decode('utf8','ignore')
    soup = BeautifulSoup(page,"lxml")

    # Collecting all articles
    text = ' '.join(map(lambda p: p.text, soup.find_all('article')))

    return text

def summarize(text, n):
    while True:
        try:
            sents = sent_tokenize(text)

            assert n <= len(sents)
            word_sent = word_tokenize(text.lower())
            _stopwords = set(stopwords.words('english') + list(punctuation))

            word_sent = [word for word in word_sent if word not in _stopwords]
            freq = FreqDist(word_sent)
            # nlargest(10, freq, key = freq.get)

            ranking = defaultdict(int)

            for i,sent in enumerate(sents):
                for w in word_tokenize(sent.lower()):
                    if w in freq:
                        ranking[i] += freq[w]

            sents_idx = nlargest(n, ranking, key=ranking.get)

            return [sents[j] for j in sorted(sents_idx)]

        except LookupError:
            print("Dependency Failure: Installing missing NLTK libraries")
            # ----------------------------------------------------- #
            # LookupError is raised when the resource punkt is missing.
            # Disable SSL context so that users on unsafe networks can download.
            # ----------------------------------------------------- #
            import nltk

            nltk.download()

if __name__ == '__main__':
    articleURL = "https://www.nytimes.com/2020/04/10/world/canada/coronavirus-canada-detroit-nurses-hospital.html"
    text = getTextArticle(articleURL)
    pprint(summarize(text, 3))
