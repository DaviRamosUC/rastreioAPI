from flask import Flask, jsonify, redirect
from flask_cors import CORS

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

@app.route('/ping', methods=['GET'])
def ping_pong():
    return jsonify('pong!')


@app.route('/search', methods=['POST'])
def search():
    return 'Funcionou'


if __name__ == '__main__':
    app.run()
