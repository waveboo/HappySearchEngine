# encoding: utf8
from flask import Flask, redirect, url_for, escape, request, jsonify
import json
from flask_cors import *
from WordCutAndCope import WordCut, InformationGet

app = Flask(__name__)
CORS(app, supports_credentials=True)

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/search', methods=['GET','POST'])
def search():
    searchKey = request.get_json()['searchKey']
    print searchKey
    Answers = dict()
    temp = InformationGet(searchKey).sentence_cope()
    for i in range(0,len(temp)):
        Answers[str(i)] = json.dumps(temp[i])
    print Answers
    print json.dumps(Answers)
    return json.dumps(Answers)

if __name__ == '__main__':
    app.run(host = '0.0.0.0')
