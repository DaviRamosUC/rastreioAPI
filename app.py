from flask import Flask, jsonify, redirect, request
from flask_cors import CORS
from api import findByCode

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
        resposta = dict(ultimoStatus=ultimoStatus, historicoArray=historicoArray, phoneNumber=phoneNumber)
    else:
        resposta = dict(ultimoStatus=ultimoStatus, historicoArray=historicoArray)
    return jsonify(resposta)


if __name__ == '__main__':
    app.run()
