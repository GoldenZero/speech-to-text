import unittest
from TextToPOS import TextToPOS, load_en_large


class TestTextToPOS(unittest.TestCase):

    def setUp(self):
        self.nlp = load_en_large()

    def test_get_post_tags(self):
       text_to_pos = TextToPOS()
       pos_tags = text_to_pos.get_filter_text('test.txt', ['VERB', 'NOUN', 'PROPN'], self.nlp)
       self.assertEqual([['love', 'VERB'], ['reading', 'NOUN'], ['books', 'NOUN'], ['library', 'NOUN']], pos_tags)