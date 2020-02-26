from flask import Flask, request

app = Flask(__name__)


@app.route('/json', methods=['POST'])
def json():
    return {}, 200
