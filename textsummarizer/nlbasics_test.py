import unittest
import nlbasics

class Testing(unittest.TestCase):
    def test_tokenizer(self):
        text = "Mary had a little lamb"
        words = nlbasics.nlbasics().do_tokenize(sample=text)
        self.assertEqual(words, ['Mary', 'had', 'a', 'little', 'lamb'])

if __name__ == '__main__':
    unittest.main()