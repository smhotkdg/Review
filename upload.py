import os
from flask import Flask, request, render_template, send_from_directory
from werkzeug.utils import secure_filename
import warnings
import pandas as pd
import re
import test
app = Flask(__name__)

APP_ROOT = os.path.dirname(os.path.abspath(__file__)) # project abs path
app.config['UPLOAD_FOLDER'] = 'D:/files/'
filePath = ''
reviewData = []


@app.route('/')
def hello_world():
    return render_template("submit.html", len = len(reviewData), result_review_value = reviewData)
@app.route('/reviewanalysis', methods=['POST', 'GET'])
def analysis(num=None):
    temp1 = request.args.get('char1')
    #print(temp1)
    result1,resultText = test.predictWeb(temp1)
    return render_template('submit.html', result = result1, result2 = str(resultText),len = len(reviewData), result_review_value = reviewData)
    #return render_template('submit.html', result = temp1, result2 = temp1)    

@app.route('/uploader', methods=['GET', 'POST'])
def uploader_file():
    
    if request.method == 'POST':
        file = request.files['file']
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], file.filename))        
        filePath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)       
        
        return fileRead(filePath)
        
def fileRead(filePath):    
    df = pd.read_excel(filePath, engine="openpyxl")
    series = df["CONTENTS"]
    series.head()
    reviewData.clear()    
    for i in range(len(series)):
        strLine =series[i].replace("\n","")
        strLine = re.sub(' +', ' ', strLine)
        #print(strLine)
        result1,resultText = test.predictWeb(strLine)
        reviewData.append((result1,resultText))
        #reviewData_Sort = result_review["content"].append(resultText)
    #reviewData_Sort = sorted(reviewData, key=lambda percent: percent[1],reverse=True)
    reviewData_Sort = sortNum(40.0,reviewData)
    return render_template('submit.html', len = len(reviewData_Sort), result_review_value = reviewData_Sort)

@app.route('/serchpercent', methods=['POST', 'GET'])
def serchpercent(num=None):
    temp1 = request.args.get('charPercet')
    floatStr = float(temp1)
    reviewData_Sort = sortNum(floatStr,reviewData)
    return render_template('submit.html', len = len(reviewData_Sort), result_review_value = reviewData_Sort)

def sortNum(num,_array):
    resultArray = []
    for i in range(len(_array)):
        if(_array[i][1] >= num):
            resultArray.append(_array[i])
    resultArray = sorted(resultArray, key=lambda percnet: percnet[1],reverse=True)   
    return resultArray
if __name__ == '__main__':
    #app.run()
    app.run(host='0.0.0.0', port=8080)    
    #