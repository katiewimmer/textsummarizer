import unittest
import nlbasics
from nltk.stem.lancaster import LancasterStemmer
from nltk.tokenize import word_tokenize

class Testing(unittest.TestCase):
    def test_tokenizer(self):
        text = "Mary had a little lamb"
        words = nlbasics.nlbasics().do_tokenize(sample=text)
        self.assertEqual(words, [['Mary', 'had', 'a', 'little', 'lamb']])

    def test_stemming(self):
        text = "I jumped into the cars quickly"

        st = LancasterStemmer()
        stemmedWords = [st.stem(word) for word in word_tokenize(text)]
        self.assertEqual(stemmedWords, ['i', 'jump', 'into', 'the', 'car', 'quick'])

if __name__ == '__main__':
    unittest.main()