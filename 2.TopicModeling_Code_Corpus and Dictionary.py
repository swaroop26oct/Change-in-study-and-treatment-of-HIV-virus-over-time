from gensim import corpora, models, similarities
from six import iteritems
from nltk.corpus import stopwords
import warnings
warnings.filterwarnings(action='ignore', category=UserWarning, module='gensim')

import csv
csvfile=open('actual_new.csv', 'r',encoding='utf-8')
rdr=csv.reader(csvfile)
stop_words=set(stopwords.words("english"))
stoplist = set('for a of the and to in'.split())
dictionary = corpora.Dictionary(row[2].lower().split() for row in rdr if len(row)>2)
stop_ids = [dictionary.token2id[stopword] for stopword in stoplist if stopword in dictionary.token2id]
stop_ids2= [dictionary.token2id[stopword] for stopword in stop_words if stopword in dictionary.token2id] 
once_ids = [tokenid for tokenid, docfreq in iteritems(dictionary.dfs) if docfreq == 1]
dictionary.filter_tokens(stop_ids + once_ids + stop_ids2)


class MyCorpus(object):
     def __iter__(self):
        with open('actual_new.csv',encoding='utf-8') as input:
            for row in csv.reader(input):
                yield dictionary.doc2bow(row[2].lower().split())
corpus = MyCorpus()
i=0
for vector in corpus:
          i=i+1

print(i)
print(dictionary)
dictionary.compactify()
dictionary.save('mytest1.dict')
cor=corpora.MmCorpus.serialize('MyDict.mm', corpus)
print('reached here')





