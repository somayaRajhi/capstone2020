from flask import Flask, request


app = Flask(__name__)


@app.route('/return_result', methods=['POST'])
def return_result():
    json_data = request.json
    if json_data is None:
        return{}, 400

    return {}, 200
