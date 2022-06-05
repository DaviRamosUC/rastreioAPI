from flask import Flask, jsonify, redirect, request
from flask_cors import CORS
from db_sqlite3 import *
from twilio.rest import Client
from scraping import findByCode
import schedule
import time
import os

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
    verifyIfHasStoredCode(code, phoneNumber, ultimoStatus[1])
    if (notify):
        resposta = dict(ultimoStatus=ultimoStatus,
                        historicoArray=historicoArray, phoneNumber=phoneNumber)
    else:
        resposta = dict(ultimoStatus=ultimoStatus,
                        historicoArray=historicoArray)
    return jsonify(resposta)


@app.route('/storedCodes', methods=['GET'])
def storedCodes():
    storedCodes = selectAll_rastreio()
    return jsonify(storedCodes)


def verifyIfHasStoredCode(code, phoneNumber, status):
    rastreios = select_rastreio(code)
    if len(rastreios) == 0:
        insere_rastreio(code, phoneNumber, status)


def verifyPerTime():
    rastreios = selectAll_rastreio()
    for rastreio in rastreios:
        code, phoneNumber, ultimoStatus = rastreio
        ultimoStatusPesquisado, historicoArray = findByCode(code)
        if ultimoStatus == "Status: Objeto entregue ao destinatário":
            remove_rastreio(code)
        elif ultimoStatus != ultimoStatusPesquisado[1]:
            atualiza_rastreio(code, ultimoStatus[1])
            sendMessage(phoneNumber)
            

def sendMessage(phoneNumber):
    print("--- Mensagem enviada para", phoneNumber)


if __name__ == '__main__':
    app.run()
    monta_tabelas()
    # schedule.every(1).hours.do(verifyPerTime)
    # while True:
    #     schedule.run_pending()
    #     time.sleep(1800)
