from flask import Flask, abort, request
import json

app = Flask(__name__)


@app.route('/empty_json')
def empty_json():
    return json.dumps({})


@app.route('/get_job/<clinet_id>')
def get_job(clinet_id):
    if len(clinet_id) == 0:
        return 'Bad Parameter', 400
    return clinet_id


@app.route('/post', methods=['POST'])
def post(clinet_id):
    json_data = request.form['json_data']
    if json_data is None:
        return 'PAGE NOT FOUND', 400

    return 'Successful!', 200
