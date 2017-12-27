# -*- coding:utf-8 -*-

from flask import Flask, redirect, url_for, escape, request, jsonify
import json
from flask_cors import *
from TypeAnalyse import Analyse
from SentenceCope.CopeWithBaidu import StartCope

app = Flask(__name__)
CORS(app, supports_credentials=True)

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/search', methods=['GET','POST'])
def search():
    searchKey = request.get_json()['searchKey']
    get = searchKey.strip()
    if(not len(get)):
        return None
    else:
        print get
        pattern = request.get_json()['pattern']
        tmp = StartCope(searchKey)
        Answers = dict()
        if (pattern == 1):
            type = Analyse().comprehend(searchKey)
        else:
            type = -1
        temp = tmp.cope(type)
        for i in range(0, len(temp)):
            Answers[str(i)] = json.dumps(temp[i])
        print Answers
        print json.dumps(Answers)
        return json.dumps(Answers)


if __name__ == '__main__':
    app.run(host = '0.0.0.0')