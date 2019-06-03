from nltk.corpus import PlaintextCorpusReader
import nltk
import textblob
import re

import pandas as pd

cr="C:\\Users\\dell\\PycharmProjects\\LBD_test\\corpus"
pmids=[]
text=[]
# with open(cr+"\\NCBI_corpus_training.txt","r") as fp:
#     strings=fp.readlines()
# for i in strings:
#     string_split=i.split('\t')
#     pmids.append(string_split[0])
#     string_split.pop(0)
#     text.append(' '.join(string_split))
#
# mydf=pd.DataFrame()
# mydf['pmid']=pmids
# mydf['text']=text
# sents_no=[]
# pmids=[]
# i=0
# for index,row in mydf.iterrows():
#     stence=row['text']
#     sents=stence.split('.')
#     newsents=[]
#     for sent in sents:
#         newsents.append(sent+'.')
#         i=i+1
#         sents_no.append(i)
#         pmids.append(row['pmid'])
#
#     # result= re.findall(r"<category=\".`+?\">(.+?)</category>",stence, re.S)
#     # print(result)
# print(sents_no)
# print(pmids)
str='you are my shine.'
str_list=list(str)
list=[]
for i in str_list:
    list.append({'str':str,"obj":"ss"})
str2=" ".join(list)
print(str2 )
wodslist = PlaintextCorpusReader(cr, '.*')

for i in wodslist.sents('NCBI_corpus_training.txt'):
    text=nltk.word_tokenize(' '.join(i))
    nltk.wordpunct_tokenize
    print(i)
    # print(nltk.pos_tag(text, tagset='universal'))