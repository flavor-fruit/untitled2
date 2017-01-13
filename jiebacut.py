# -*- coding: utf-8 -*-
import jieba
import jieba.posseg as pseg
import numpy as np
import pynlpir
import lda
import os
import codecs
import sys
reload(sys)
sys.setdefaultencoding('utf8')

filepath = r'D:\data1'
stopwords = codecs.open('stopword.txt', 'r', encoding='utf-8')
stopword_list = []
all_words = []
vector=[]
dict_array=[]
for word in stopwords.read().split('\n'):
    stopword_list.append(word.strip())

for filename in os.listdir(filepath):
    file = codecs.open(filepath + '\\' + filename, 'r', encoding='utf-8')
    abstract = file.read()
    words = pseg.cut(abstract)

    cutwords=[]
    for word in words:
        cutwords.append(word.word)
    line = ' '.join(cutwords)
    result = codecs.open(r'D:\jieba' + '\\' + filename, 'w',encoding='utf-8')
    result.write(line)
    delstopword_list = []
    for word in cutwords:
        singleword = word
        if singleword not in stopword_list:

            if singleword >= u'\u4e00' and singleword <= u'\u9fa5':  # 判断是否是汉字
                delstopword_list.append(singleword)
                all_words.append(singleword)

    delstopwords = ' '.join(delstopword_list)
    delpath = codecs.open(r'D:\clean' + '\\' + filename, 'w',encoding='utf-8')
    delpath.write(delstopwords)



    TF_dic = dict.fromkeys(delstopword_list,0)
    for word in delstopword_list:
        word = word.strip()
        TF_dic[word]+=1
    TF_result = codecs.open(r'D:\TF' + '\\' + filename, 'w',encoding='utf-8')
    dict_array.append(TF_dic)
    for a,b in TF_dic.items():
        if b > 0:
            TF_result.write(a + '\t' + str(b).encode('utf-8') + '\n')

words_set = list(set(all_words))
print len(words_set)
vector_array=[]

for i in dict_array:
    vector = []
    for word in words_set:
        if word in i:
            vector.append(i[word])
        else:
            vector.append(0)
    vector_array.append(vector)

X = np.array(vector_array)

model = lda.LDA(n_topics=2, n_iter=1500, random_state=1)
model.fit(X)

topic_word = model.topic_word_
print("type(topic_word): {}".format(type(topic_word)))
print("shape: {}".format(topic_word.shape))

n = 10
for i, topic_dist in enumerate(topic_word):
    topic_words = np.array(words_set)[np.argsort(topic_dist)]
    print('*Topic {}\n- {}'.format(i, ' '.join(topic_words)))

doc_topic = model.doc_topic_
print("type(doc_topic): {}".format(type(doc_topic)))
print("shape: {}".format(doc_topic.shape))

for n in range(10):
    topic_most_pr = doc_topic[n]
    print("doc: {} topic: {}".format(n, topic_most_pr))

def cutword(filepath):
    #filepath = r'C:\Users\f\PycharmProjects\wanfang\data'
    for filename in os.listdir(filepath):
        file = codecs.open(filepath + '\\' + filename, 'r', encoding='utf-8')
        abstract = file.read()
        words = pynlpir.segment(abstract)
        result = codecs.open(r'D:\fenci' + '\\' + filename, 'w')
        result.write(repr(words))

def delstopword(filepath):
    stopwords = codecs.open('stopword.txt', 'r', encoding='utf-8')
    stopword_list = []
    for filename in os.listdir(filepath):
        file = codecs.open(filepath + '\\' + filename, 'r', encoding='utf-8')
        words = file.read()
        print words[0]
        delstopword_list = []
        for word in words:
            # print word[0].strip()
            if word[0] not in stopword_list:
                if word[0] >= u'\u4e00' and word[0] <= u'\u9fa5':  # 判断是否是汉字
                    delstopword_list.append(word[0])
                    print word[0]


file = codecs.open(r'C:\Users\f\PycharmProjects\wanfang\data\1.txt', 'r', encoding='utf-8')
s=file.read()
for w in pseg.cut(s):
     print w.word #加词性标注

