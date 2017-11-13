import spacy


class TextToPOS:
    def get_filter_text(self, text_file, nlp):
        with open(text_file, "r") as fh:
            text = fh.read()
            doc = nlp(text)

        return [[w.text, w.pos_] for w in doc if w.pos_ in ['VERB', 'NOUN', 'PROPN'] ]

    @staticmethod
    def load_en_large():
        return spacy.load('en_core_web_lg')
