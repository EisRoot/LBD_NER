import pandas as pd

class SentenceGetter(object):

    def __init__(self, data):
        self.n_sent = 0
        self.data = data
        self.empty = False
        agg_func = lambda s: [(str(w), p, t) for w, p, t in zip(s["WORD"].values.tolist(),
                                                           s["POS"].values.tolist(),
                                                           s["CAT"].values.tolist())]
        self.grouped = self.data.groupby("SENT_NO").apply(agg_func)
        self.sentences = [s for s in self.grouped]

    def get_next(self):
        try:
            s = self.grouped[str(self.n_sent)]
            self.n_sent += 1
            return s
        except:
            return None

def word2features(sent, i):

    word = sent[i][0]
    postag = sent[i][1]
    features = {
    'bias': 1.0,
    'word.lower()': word.lower(),
    'word[-3:]': word[-3:],
    'word[-2:]': word[-2:],
    'word.isupper()': word.isupper(),
    'word.istitle()': word.istitle(),
    'word.isdigit()': word.isdigit(),
    'word':word,
    'postag': postag,

    }
    if i > 0:
        word1 = sent[i-1][0]
        postag1 = sent[i-1][1]
        features.update({
        '-1:word.lower()': word1.lower(),
        '-1:word.istitle()': word1.istitle(),
        '-1:word.isupper()': word1.isupper(),
        '-1:postag': postag1,
        '-1:postag[:2]': postag1[:2],
        })
    else:features['BOS'] = True
    if i < len(sent)-1:
        word1 = sent[i+1][0]
        postag1 = sent[i+1][1]
        features.update({
        '+1:word.lower()': word1.lower(),
        '+1:word.istitle()': word1.istitle(),
        '+1:word.isupper()': word1.isupper(),
        '+1:postag': postag1,
        })
    else:features['EOS'] = True
    return features
def sent2features(sent):
    return [word2features(sent, i) for i in range(len(sent))]
def sent2labels(sent):
    return [label for token, postag, label in sent]
def sent2tokens(sent):
    return [token for token, postag, label in sent]


corpus=pd.read_csv('C:\\Users\\dell\\PycharmProjects\\LBD_test\\NCBI_corpus_trainset.csv',index_col=0,dtype='str')

getter=SentenceGetter(corpus)
sentences = getter.sentences
X = [sent2features(s) for s in sentences]
y = [sent2labels(s) for s in sentences]
# import matplotlib.pyplot as plt
# plt.style.use("ggplot")
# plt.hist([len(s) for s in sentences], bins=120)
# plt.show()
words = list(set(corpus["WORD"].values))
tags = list(set(corpus["CAT"].values))
