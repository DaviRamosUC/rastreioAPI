"""@file main.py
Arquivo responsável por realizar a entrada no sistema
"""
# @file main.py
# Imports
from flask import Flask, jsonify, render_template, request
from flask_cors import CORS
from db_sqlite3 import *
from scraping import findByCode
import schedule
import time
import threading
import os
from twilio.rest import Client

# Inicia o app
app = Flask(__name__, static_folder="./App/dist/assets",
            template_folder="./App/dist")
app.config.from_object(__name__)

# habilita CORS
CORS(app, resources={r'/*': {'origins': '*'}})


@app.route('/', methods=['GET'])
def home():
    """
    Função responsável por redirecionar para o html de entrada
    :return Html
    """
    return render_template("index.html")


@app.route('/search', methods=['POST'])
def search():
    """
    Função responsável por realizar o rastreio
    :return json
    """
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
    """
    Função responsável retornar dados da tabela
    :return json
    """
    storedCodes = selectAll_rastreio()
    return jsonify(storedCodes)


@app.route('/removeCode/<code>', methods=['DELETE'])
def deleteCode(code):
    """
    Função responsável por chamar a função que deleta um dado na tabela
    :return json
    """
    response_object = {'status': 'success'}
    response_object['message'] = remove_rastreio(code)
    return jsonify(response_object)


def verifyIfHasStoredCode(code, phoneNumber, status):
    """
    Função responsável por verificar se já existe o rastreio na tabela
    """
    rastreios = select_rastreio(code)
    if len(rastreios) == 0:
        insere_rastreio(code, phoneNumber, status)


def verifyPerTime():
    """
    Função responsável por verificar mudança do rastrio na web por determinado tempo
    """
    rastreios = selectAll_rastreio()
    for rastreio in rastreios:
        code, phoneNumber, ultimoStatus = rastreio
        ultimoStatusPesquisado, historicoArray = findByCode(code)
        if ultimoStatus != ultimoStatusPesquisado[1]:
            atualiza_rastreio(code, ultimoStatusPesquisado[1])
            sendMessage(phoneNumber, ultimoStatusPesquisado[1])


def sendMessage(phoneNumber, status):
    """
    Função responsável por enviar mensagem sms para usuário
    :param phoneNumber: String contendo o número de celular informado pelo usuário
    :param status: String contendo o último status
    """
    os.environ['TWILIO_ACCOUNT_SID'] = 'AC003bf8c7784b5cdb6c445f08b727b7f9'
    os.environ['TWILIO_AUTH_TOKEN'] = '1e7182dbc2265d4c232dfdbcf9e859d6'
    account_sid = os.environ['TWILIO_ACCOUNT_SID']
    auth_token = os.environ['TWILIO_AUTH_TOKEN']
    client = Client(account_sid, auth_token)

    message = client.messages.create(
        body='O rastreio do seu pacote foi atualizado, ' + status,
        from_='+19706968659',
        to='+5571991360431'
    )


def continueJob():
    """
    Função responsável por manter o schedule rodando
    """
    schedule.every(1).minutes.do(verifyPerTime)
    while True:
        schedule.run_pending()
        time.sleep(1)


def mainJob():
    """
    Função responsável por rodar o Flask em segunda thread
    """
    app.run(debug=False)


def multithread(func):
    """
    Função responsável por criar multithreads
    """
    job = threading.Thread(target=func)
    job.start()


if __name__ == '__main__':
    """
    Função responsável por main
    """
    monta_tabelas()
    multithread(mainJob)
    multithread(continueJob)