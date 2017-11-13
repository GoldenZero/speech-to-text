import unittest
from TextToPOS import TextToPOS


class TestTextToPOS(unittest.TestCase):

    def setUp(self):
        self.nlp = TextToPOS.load_en_large()

    def test_get_post_tags(self):
       text_to_pos = TextToPOS()
       pos_tags = text_to_pos.get_filter_text('simple_test.txt', self.nlp)
       self.assertEqual([['love', 'VERB'], ['read', 'VERB'], ['books', 'NOUN'], ['library', 'NOUN']], pos_tags)