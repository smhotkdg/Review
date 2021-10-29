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
model= models.load_model("../my_model.h5")
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
    if(score > 0.5):
        return ("["+review+"]"),  ("{:.2f}% 확률로 긍정 리뷰".format(score * 100))        
    else:
        return ("["+review+"]"),  ("{:.2f}% 확률로 부정 리뷰".format((1-score) * 100))
    #print(time.time()-start)
predict_pos_neg("맛있어요")
predict_pos_neg("^^")
predict_pos_neg("배송이 느려요")
predict_pos_neg("배송이 빨라요")
predict_pos_neg("맛없어요")
predict_pos_neg("싱싱해요")
predict_pos_neg("상했어요")
predict_pos_neg("뭐.....")
predict_pos_neg("무난")
predict_pos_neg("애호박이 얼어서 왔네요")
predict_pos_neg("애호박이 얼어서 개짱나네")
predict_pos_neg("개꿀맛")
predict_pos_neg("ㅗㅗ")
predict_pos_neg("야채는 싱싱함이 최고죠")
predict_pos_neg("휘뚜루 마뚜루")
predict_pos_neg("콩나물이 다 물러지고 상한 냄새 나서 못 먹었어요")
predict_pos_neg("가성비 짱")
predict_pos_neg("아쉬워요")
predict_pos_neg("이런상태로?")
predict_pos_neg("냄새 안난다는 평보고 샀는데 입맛 까다롭지 않은 남편도 누린내 난다하네요.저는 냄새에 좀 민감해서 누린내 안나게 할려고 깻잎도 넣고 청량도 하나 넣었는데ㅠ")
predict_pos_neg("조리할 때 짤까봐 물을 좀 부어서 그런건지는 모르겠지만 고기 누린내가 많이나서 후추를 뿌려서 먹었어요. 다음엔 안시켜먹을 것 같네요. 고기 양은 많았습니다.")
predict_pos_neg("매웠어요. 애들이먹기에는")
predict_pos_neg("으로 먹기 좋아요 거의 매번 사는 것 같네요")
predict_pos_neg("후기도 좋고 고구마 치즈 조합 좋아해서 사봤어요")
predict_pos_neg("2개 샀는데 1개 먹고 그냥저냥인 것 같아.. 1개는 계속 냉동실에 있어요 ㅠ")
predict_pos_neg("컬리 돌 바나나 저렴하고 달아서 자주 구매해요.이번엔 첨으로 비닐포장도 없이 왔네요 ㅡㅡ좀 덜 싱싱해보이고 비닐포장도 없어 좀 찜찜하지만,믿습니다.")
predict_pos_neg("남편은 맵다고 하는데,저는 딱 좋았어요")
predict_pos_neg("바나나 처음 시켜보는데 안익은거 보내주시네요 ㅠㅠ바로 먹고 싶었는데 익는동안 다른거 사먹어야 할듯요")