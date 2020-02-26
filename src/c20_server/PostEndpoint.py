from flask import Flask, jsonify, request #import objects from the Flask model
app = Flask(__name__) #define app using Flask



@app.route('/empty_json')
def empty_json():
    return jsonify ({})



@app.route('/get_work', methods=['POST'])
def get_work();
 if not request.json;
        abort(400)

return jsonify({}), 200
