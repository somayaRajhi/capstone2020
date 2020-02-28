from flask import Flask, abort, request
import json

app = Flask(__name__)


@app.route('/empty_json')
def empty_json():
    return json.dumps({})

@app.route('/get_job')
def get_job():
    clinet_id=request.args['clinet_id']
    if clinet_id != 'soma':
        return {},403
    return {},200
