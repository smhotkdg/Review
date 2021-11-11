import os
from flask import Flask, request, render_template, send_from_directory
from werkzeug.datastructures import Range
from werkzeug.utils import secure_filename
import warnings
import pandas as pd
import re
from ast import literal_eval
import test
import json
app = Flask(__name__)

APP_ROOT = os.path.dirname(os.path.abspath(__file__)) # project abs path
app.config['UPLOAD_FOLDER'] = 'D:/files/'
filePath = ''
reviewData = []
CompareNumber = 70

@app.route('/')
def hello_world():
    return render_template("submit.html", range = 70)
@app.route('/reviewanalysis', methods=['POST', 'GET'])
def analysis(num=None):
    temp1 = request.args.get('char1')
    
    #result1,resultText = test.predictWeb(temp1)
    #return render_template('submit.html', result = result1, result2 = str(resultText),len = len(reviewData), result_review_value = reviewData)
    
def sortNum(num,_array):
    resultArray = []
    for i in range(len(_array)):
        if(int(_array[i][1]) >= num):
            resultArray.append(_array[i])
    resultArray = sorted(resultArray, key=lambda percnet: percnet[1],reverse=True)   
    return resultArray

@app.route('/uploader', methods=['GET', 'POST'])
def uploader_file():            
    if request.method == 'POST':
        file = request.files['file']
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], file.filename))        
        filePath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)       
        
        return fileRead(filePath)
@app.route('/keywordCheck', methods=['GET', 'POST'])
def KeywordCheck():
    Keywords = []
    reviewData_Sort = sortNum(0,reviewData)
    testKeyword =request.form['keyworkdArea']
    testKeyword = testKeyword.replace(" ","")
    testKeyword = testKeyword.replace("\n","")
    Keywords.clear()
    Keywords = testKeyword.split(",")        

    reviewData_Sort = sortNum(0,reviewData)
    #print(len(Keywords))
    if(len(Keywords)>0 and Keywords[0]!=""):
        for i in range(len(reviewData_Sort)):        
            #print(any(keyword in reviewData_Sort[i][0] for keyword in Keywords))
            if(any(keyword in reviewData_Sort[i][0] for keyword in Keywords)==True):            
                temp = list(reviewData_Sort[i])
                temp[1] = 100
                reviewData_Sort[i] = temp
        #print(reviewData_Sort)
        reviewData_Sort = sortNum(0,reviewData_Sort)
    #print(reviewData_Sort)
    return render_template('submit.html',flash_message="True",flaskvar = reviewData_Sort,range = CompareNumber)    


@app.route('/testFunction', methods=['GET', 'POST'])
def testFunction(inputData):        
 
    
    return render_template('submit.html',flash_message="True",flaskvar = inputData,range = CompareNumber)

@app.route('/testFunction2', methods=['GET', 'POST'])
def testFunction2():          
    reviewData.clear()
    
    reviewData.append(["1","98","Dissatisfaction","0"])
    reviewData.append(["2","98","Normal","1"])    
    reviewData.append(["2","98","Normal","1"])   
    return render_template('submit.html',flash_message="True",flaskvar = reviewData,range = CompareNumber)
@app.route('/setRange', methods=['GET', 'POST'])
def setRangeFunction():
    if(request.form['setRangeArea']==""):
        CompareNumber = 70
    else:        
        CompareNumber =int(request.form['setRangeArea'])
    RangeData = sortNum(0,reviewData)
    print(CompareNumber)
    for i in range(len(RangeData)):
        compareValue =0        
        if(int(RangeData[i][1]) >=CompareNumber):            
            if(str(RangeData[i][2]) == "Normal"):
                compareValue =1
            else:
                compareValue =0
        else:            
            if(str(RangeData[i][2]) == "Normal"):
                compareValue =0
            else:
                compareValue =1
        temp = list(RangeData[i])
        temp[3] = compareValue
        RangeData[i] = temp    

    return render_template('submit.html',flash_message="True",flaskvar = RangeData,range = CompareNumber)
@app.route('/Loading', methods=['GET', 'POST'])
def loading():
    return render_template('submit.html',HoitTest ="이제 시작한다")


def fileRead(filePath):            
    
    file_Compare = open('../compareData.txt', 'at',encoding='UTF8')
    df = pd.read_excel(filePath, engine="openpyxl")
    series = df["CONTENTS"]
    series_type = df["REVIEWS_TYPE"]
    series.head()
    series_type.head()
    reviewData.clear()    
    compareValue = 0
    for i in range(len(series)):
        strLine =series[i].replace("\n","")
        strLine = re.sub(' +', ' ', strLine)
        strLine = strLine.replace(","," ")
        #print(strLine)
        result1,resultText = test.predictWeb(strLine)
        result1 = result1.replace(","," ")
        
        if(resultText >=CompareNumber):
            str_compare = strLine+" "+str(series_type[i])+" "+ str("부정  ")+  str(resultText)+"\n"
            if(str(series_type[i]) == "Normal"):
                compareValue =1
            else:
                compareValue =0
        else:
            str_compare = strLine+" "+str(series_type[i])+" "+ str("긍정  ")+str(resultText)+"\n"
            if(str(series_type[i]) == "Normal"):
                compareValue =0
            else:
                compareValue =1
        file_Compare.write(str_compare)           
     
        #compareValue ==0 이면 평가가 일치함 1이면 일치하지 않음
        reviewData.append((result1,resultText,str(series_type[i]),compareValue))
        #reviewData_Sort = result_review["content"].append(resultText)
    #reviewData_Sort = sorted(reviewData, key=lambda percent: percent[1],reverse=True)    
    
    reviewData_Sort = sortNum(0,reviewData)
    
    file_Compare.close()
    #return render_template('submit.html', len = len(reviewData_Sort), result_review_value = reviewData_Sort)]
    
    return testFunction(reviewData_Sort) 

@app.route('/serchpercent', methods=['POST', 'GET'])
def serchpercent(num=None):
    temp1 = request.args.get('charPercet')
    floatStr = float(temp1)
    reviewData_Sort = sortNum(floatStr,reviewData)
    return render_template('submit.html', len = len(reviewData_Sort), result_review_value = reviewData_Sort)


if __name__ == '__main__':
    #app.run()
    app.run(host='0.0.0.0', port=8080)    
    #