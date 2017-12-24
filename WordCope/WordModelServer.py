# -*- coding:utf-8 -*-

from flask import Flask
from flask import request
from flask import jsonify
from WordModel import Model
app = Flask(__name__)

model = Model()


@app.route("/", methods=['POST'])
def index():
    sentence = request.form['sentence']
    return jsonify({'vec': list(model.sentence_vector(sentence))})

@app.route("/dict", methods=['POST'])
def importdict():
    model.load_dict()
    return 'Load Complete'

if __name__ == "__main__":
    app.run(port=8888)
