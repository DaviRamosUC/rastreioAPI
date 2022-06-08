from flask import Flask, jsonify, render_template, request
from flask_cors import CORS
from db_sqlite3 import *
from scraping import findByCode
import schedule
import time
import os
from twilio.rest import Client

# configuration
DEBUG = True

# instantiate the app
app = Flask(__name__, static_folder="./App/dist/assets", template_folder="./App/dist")
app.config.from_object(__name__)

# enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})


@app.route('/', methods=['GET'])
def home():
    # return redirect("http://localhost:3000/", code=302)
    return render_template("index.html")


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


@app.route('/removeCode/<code>', methods=['DELETE'])
def deleteCode(code):
    response_object = {'status': 'success'}
    response_object['message'] = remove_rastreio(code)
    return jsonify(response_object)


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
    os.environ['TWILIO_ACCOUNT_SID'] = 'AC003bf8c7784b5cdb6c445f08b727b7f9'
    os.environ['TWILIO_AUTH_TOKEN'] = '42bffa188579b9da4d53f3f92e5dff69'
    account_sid = os.environ['TWILIO_ACCOUNT_SID']
    auth_token = os.environ['TWILIO_AUTH_TOKEN']
    client = Client(account_sid, auth_token)

    message = client.messages.create(
                              body='ISSO É UM TESTE',
                              from_='+19706968659',
                              to='+55'+phoneNumber
                          )


if __name__ == '__main__':
    sendMessage('21964104892')
    # app.run()
    # monta_tabelas()
    # schedule.every(1).hours.do(verifyPerTime)
    # while True:
    #     schedule.run_pending()
    #     time.sleep(1800)
