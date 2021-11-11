import random
with open('../Files/train.txt','r',encoding='UTF8') as source:
    data = [ (random.random(), line) for line in source ]
data.sort()
with open('../Files/train_Shuffle.txt','w',encoding='UTF8') as target:
    for _, line in data:
        target.write( line )