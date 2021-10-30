import csv
import re

def file_len(fname):
    i =0
    with open(fname,encoding='UTF8') as f:
        for i, l in enumerate(f):
            pass
    return i + 1


file_rating_train_negative = open('../ratings_train_reviewNegative.txt', 'at',encoding='UTF8')
file_rating_train_Positive = open('../ratings_train_reviewPositive.txt', 'at',encoding='UTF8')
file_rating_train_Best = open('../ratings_train_reviewBest.txt', 'at',encoding='UTF8')


negativeCount=0
positiveCount =0
for i in range(27):
    strFileNumber = str(i+1)
    f = open('D:/reviewData/review_10/'+strFileNumber+'.csv','r',encoding='UTF8')
    rdr = csv.reader(f)
    for line in rdr:
        line_pov = "0"
        line_content = ""    
        positiveCount+=1
        if(line[2]=="Normal"):            
            #countPositive = file_len('../ratings_train_reviewPositive.txt')
            line_pov = "1"    
            strLine =line[1].replace("\n"," ")
            strLine = re.sub(' +', ' ', strLine)
            line_content =str(positiveCount)+"\t"+strLine+"\t"+line_pov+"\n"
            file_rating_train_Positive.write(line_content)
        elif(line[2]=="Best"):
            line_pov = "0"    
            strLine =line[1].replace("\n"," ")
            strLine = re.sub(' +', ' ', strLine)
            line_content =str(positiveCount)+"\t"+strLine+"\t"+line_pov+"\n"
            file_rating_train_Best.write(line_content)
        else:
            strLine =line[1].replace("\n"," ")
            strLine = re.sub(' +', ' ', strLine)
            #countNegative = file_len('../ratings_train_reviewNegative.txt')            
            line_content =str(positiveCount)+"\t"+strLine+"\t"+line_pov+"\n"
            file_rating_train_negative.write(line_content)
        
f.close()
file_rating_train_negative.close()
file_rating_train_Positive.close()


