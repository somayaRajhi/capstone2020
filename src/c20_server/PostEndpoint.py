from flask import Flask, abort, request #import objects from the Flask model
import json


app = Flask(__name__) #define app using Flask


@app.route('/empty_json')
def empty_json():
        if not request.json:
            abort(400)
    return json.dumps({}),200

@app.route('/get_job', methods=['POST'])
def get_work():
    json_data=rerequest.form['json']
    ##json_data=request.args.get['json_data']////
    if json_data is None:
        return abort(400)

    return json.dumps({json_data}), 200
