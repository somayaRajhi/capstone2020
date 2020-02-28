from flask import Flask, abort, request
import json

app = Flask(__name__)


@app.route('/empty_json')
def empty_json():
    return json.dumps({})



@app.route('/get_job')
def get_job():
    client_id = request.args['client_id']
    if client_id != 'soma':
        return {}, 403
    return {}, 200


@app.route('/return_result', methods=['POST'])
def return_result():
    json_data = request.form['json_data']
    if json_data is None:
        return {}, 400
    return {}, 200


