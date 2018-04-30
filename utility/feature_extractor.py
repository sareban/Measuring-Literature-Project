import sklearn.feature_extraction.text


class TextFeature(object):
    '''
    This class is to create feature matrix
    '''

    def __init__(self, corpus, analyzer='word', ngram=(1, 1), idf=False, norm=None, binary=False):
        tfm = sklearn.feature_extraction.text.TfidfVectorizer(use_idf=idf, analyzer=analyzer, tokenizer=str.split,
                                                              ngram_range=ngram, norm=norm,
                                                              stop_words=[], lowercase=False, binary=binary)
        self.tf_vec = tfm.fit_transform(corpus)
        self.feature_names = tfm.get_feature_names()


