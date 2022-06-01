from flask import Flask, jsonify, redirect, request
from flask_cors import CORS
from scraping import findByCode
from db_sqlite3 import *

# configuration
DEBUG = True

# instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)

# enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})


@app.route('/', methods=['GET'])
def home():
    return redirect("http://localhost:3000/", code=302)


@app.route('/search', methods=['POST'])
def search():
    code = request.form.get('code')
    phoneNumber = request.form.get('phoneNumber')
    notify = request.form.get('sms')
    searchData = findByCode(code)
    ultimoStatus, historicoArray = searchData
    if (notify):
        resposta = dict(ultimoStatus=ultimoStatus,
                        historicoArray=historicoArray, phoneNumber=phoneNumber)
        insere_rastreio(code, phoneNumber, ultimoStatus[1])
    else:
        resposta = dict(ultimoStatus=ultimoStatus,
                        historicoArray=historicoArray)
        insere_rastreio(code, None, ultimoStatus[0])
    return jsonify(resposta)


@app.route('/storedCodes', methods=['GET'])
def storedCodes():
    storedCodes = selectAll_rastreio()
    return jsonify(storedCodes)


if __name__ == '__main__':
    app.run()
    monta_tabelas()
