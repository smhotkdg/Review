#-*- coding: utf-8 -*-
import json
import os
from pprint import pprint
from konlpy.tag import Okt
import nltk
import matplotlib.pyplot as plt
from matplotlib import font_manager, rc
import numpy as np

from tensorflow.keras import models
from tensorflow.keras import layers
from tensorflow.keras import optimizers
from tensorflow.keras import losses
from tensorflow.keras import metrics
import time
start = time.time()
#%matplotlib inline

def read_data(filename):
    with open(filename, 'rt',encoding='UTF8') as f:
        data = [line.split('\t') for line in f.read().splitlines()]
        # txt 파일의 헤더(id document label)는 제외하기
        data = data[1:]
    return data
train_data = read_data('../ratings_train.txt')
test_data = read_data('../ratings_test.txt')

okt = Okt()
#print(okt.pos(u'필리핀가서 사기치고 다녔네 역시 회개는 얼어죽을 한번깡패는 영원한 깡패지 깡패 미화영화는 사라져야'))

def tokenize(doc):
    # norm은 정규화, stem은 근어로 표시하기를 나타냄
    return ['/'.join(t) for t in okt.pos(doc, norm=True, stem=True)]

if os.path.isfile('../train_docs.json'):
    with open('../train_docs.json',encoding="utf-8") as f:
        train_docs = json.load(f)
    with open('../test_docs.json',encoding="utf-8") as f:
        test_docs = json.load(f)
else:
    train_docs = [(tokenize(row[1]), row[2]) for row in train_data]
    test_docs = [(tokenize(row[1]), row[2]) for row in test_data]
    # JSON 파일로 저장
    with open('../train_docs.json', 'w', encoding="utf-8") as make_file:
        json.dump(train_docs, make_file, ensure_ascii=False, indent="\t")
    with open('../test_docs.json', 'w', encoding="utf-8") as make_file:
        json.dump(test_docs, make_file, ensure_ascii=False, indent="\t")

tokens = [t for d in train_docs for t in d[0]]
text = nltk.Text(tokens, name='NMSC')


selected_words = [f[0] for f in text.vocab().most_common(10000)]

def term_frequency(doc):
    return [doc.count(word) for word in selected_words]

# Save the entire model to a HDF5 file
model= models.load_model("../review_model8.h5")
def predict_pos_neg(review):
    #start = time.time()
    token = tokenize(review)
    tf = term_frequency(token)
    data = np.expand_dims(np.asarray(tf).astype('float32'), axis=0)    
    score = float(model.predict(data))
    if(score > 0.5):
        print("[{}\n {:.2f}% 확률로 긍정 리뷰\n".format(review, score * 100))
    else:
        print("[{}]\n {:.2f}% 확률로 부정 리뷰\n".format(review, (1 - score) * 100))
    #print(time.time()-start)

def predictWeb(review):
    #start = time.time()
    token = tokenize(review)
    tf = term_frequency(token)
    data = np.expand_dims(np.asarray(tf).astype('float32'), axis=0)    
    score = float(model.predict(data))
    # if(score > 0.5):
    #     return ("["+review+"]"),  ("{:.2f}%".format(score * 100))        
    # else:
    
    #print(("["+review+"]"),  round((1-score) * 100))
    return review,  round((1-score) * 100)
    #print(time.time()-start)

# files = open('../trainData/test.txt', 'r',encoding='UTF8')

# while True:
#     line = files.readline()
#     if not line: break    
#     print(predictWeb(line))    
# files.close()
# Negative_equal = open('../Negative_equal.txt', 'at',encoding='UTF8')
# Negative_Not_equal = open('../Negative_Not_equal.txt', 'at',encoding='UTF8')

# Positive_equal = open('../Positive_equal.txt', 'at',encoding='UTF8')
# Positive_Not_equal = open('../Positive_Not_equal.txt', 'at',encoding='UTF8')

# file_Natative = open('../ratings_train_reviewNegative.txt', 'r',encoding='UTF8')
# file_Positive = open('../ratings_train_reviewPositive.txt', 'r',encoding='UTF8')


# lines = file_Natative.readlines()
# count =0
# for line in lines:    
#     strLine =line.replace("\t","")
#     strLine =line.replace("0","")    
#     new_string = strLine[1:]
#     review,percent = predictWeb(new_string)
#     count+=1    
  
#     #print("======"+str(count) +"=====")
#     if(percent>70):
#         print("======"+str(count) +"===== Negative Equal")
#         Negative_equal.write(new_string)        
#     else:
#         print("======"+str(count) +"===== Negative Not Equal")
#         Negative_Not_equal.write(new_string)
# Negative_Not_equal.close()
# Negative_equal.close()
# file_Natative.close()
# Positvelines = file_Positive.readlines()
# for line in Positvelines:   
#     strLine =line.replace("\t","")
#     strLine =line.replace("1","")
#     review,percent = predictWeb(strLine)

#     count+=1  
#     #print("======"+str(count) +"=====")
#     if(percent<=1):
#         print("======"+str(count) +"===== Positive Equal")
#         Positive_equal.write(strLine)
#     else:
#         print("======"+str(count) +"===== Positive Not Equal")
#         Positive_Not_equal.write(strLine)
# Positive_equal.close()
# Positive_Not_equal.close()
# file_Positive()