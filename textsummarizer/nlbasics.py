import nltk
from pprint import pprint

# Tokenizing module
from nltk.tokenize import word_tokenize, sent_tokenize
# Stopwords module
from nltk.corpus import stopwords
from string import punctuation
# Bigrams module
from nltk.collocations import *
# Stemming module
from nltk.stem.lancaster import LancasterStemmer
# Disambiguation module
from nltk.corpus import wordnet as wn
from nltk.wsd import lesk

class nlbasics():

    # Tokenizing text
    def do_tokenize(self):
        text = input ("Enter your text to tokenize here: ")
        
        sents = sent_tokenize(text)
        # print(sents)

        words = [word_tokenize(sent) for sent in sents]
        return words

    # Removing stopwords
    def do_removestopwords(self):
        text = input ("Enter your text here: ")

        customStopWords = set(stopwords.words('english')+list(punctuation))
        wordsWOStopwords = [word for word in word_tokenize(text) if word not in customStopWords]
        return wordsWOStopwords

    #Identifying bigrams
    def do_identifybigrams(self):
        text = input ("Enter your text here: ")

        customStopWords = set(stopwords.words('english')+list(punctuation))
        wordsWOStopwords = [word for word in word_tokenize(text) if word not in customStopWords]
        
        bigram_measures = nltk.collocations.BigramAssocMeasures()
        finder = BigramCollocationFinder.from_words(wordsWOStopwords)
        return finder.ngram_fd.items()

    # Stemming
    def do_stemming(self):
        text = input ("Enter your text here: ")

        st = LancasterStemmer()
        stemmedWords = [st.stem(word) for word in word_tokenize(text)]
        return stemmedWords

    # POS Tagging
    def do_POStagging(self):
        text = input ("Enter your text here: ")

        tagList = nltk.pos_tag(word_tokenize(text))
        return tagList

    # Disambiguating word meanings
    def do_worddisambiguation(self):
        word = input ("Enter your word here: ")
        for ss in wn.synsets(word):
            print(ss, ss.definition())

        text2 = input ("Enter a sentence with that previous word: ")
        contextualsentence = lesk(word_tokenize(text2), word)
        return [contextualsentence, contextualsentence.definition()]

if __name__ == '__main__':
    menu = """
    1: Tokenize text
    2: Remove stopwords
    3: Find bigrams
    4: Word stemmer
    5: Part of speech tagging
    6: Word disambiguation (must enter single word)
    """

    print(menu)

    mymenu = nlbasics()

    choice = input ("Input your choice [1]: " )

    if choice == "2":
        print(mymenu.do_removestopwords())
    elif choice == "3":
        print(mymenu.do_identifybigrams())
    elif choice == "4":
        print(mymenu.do_stemming())
    elif choice == "5":
        print(mymenu.do_POStagging())
    elif choice == "6":
        print(mymenu.do_worddisambiguation())
    else:
        print(mymenu.do_tokenize())