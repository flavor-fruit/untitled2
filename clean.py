# -*- coding: utf-8 -*-
import pynlpir
import os
import codecs

filepath = r'C:\Users\f\PycharmProjects\wanfang\data'
stopwords = codecs.open('stopword.txt', 'r', encoding='utf-8')
stopword_list = []

for word in stopwords.read().split('\n'):
    stopword_list.append(word.strip())
pynlpir.open()
for filename in os.listdir(filepath):
    file = codecs.open(filepath + '\\' + filename, 'r', encoding='utf-8')
    abstract = file.read()
    words = pynlpir.segment(abstract)

    cutwords=[]
    for word in words:
        cutwords.append(word[0])
    line = ' '.join(cutwords)
    result = codecs.open(r'D:\fenci' + '\\' + filename, 'w',encoding='utf-8')
    result.write(line)
    delstopword_list = []
    for word in words:
        #print word[0].strip()
        if word[0] not in stopword_list:
            if word[0] >= u'\u4e00' and word[0] <= u'\u9fa5':  # 判断是否是汉字
                delstopword_list.append(word[0])
                print word[0]
    delstopwords = ' '.join(delstopword_list)
    delpath = codecs.open(r'D:\clean' + '\\' + filename, 'w',encoding='utf-8')
    delpath.write(delstopwords)


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