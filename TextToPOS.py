import spacy


@staticmethod
def load_en_large():
    return spacy.load('en_core_web_lg')


class TextToPOS:
    def get_filter_text(self, text_file, pos_tags, nlp):
        text = open().read(text_file)
        doc = nlp(text)

        return [[w, w.pos_] for w in doc if w.pos_ in ['VERB', 'NOUN', 'PROPN'] ]


