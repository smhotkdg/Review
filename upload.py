import os
from flask import Flask, request, render_template, send_from_directory
import test
app = Flask(__name__)

APP_ROOT = os.path.dirname(os.path.abspath(__file__)) # project abs path

@app.route('/')
def hello_world():
    return render_template("submit.html")
@app.route('/calculate', methods=['POST', 'GET'])
def calculate(num=None):
    temp1 = request.args.get('char1')
    print(temp1)
    result1,resultText = test.predictWeb(temp1)
    return render_template('submit.html', result = result1, result2 = resultText)
    #request.args.set('result') = temp1
    #return temp1
    #return test.predictWeb(temp1)
if __name__ == '__main__':
    #app.run()
    app.run(host='0.0.0.0', port=8080)