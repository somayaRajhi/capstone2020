from flask import Flask, request

app = Flask(__name__)


@app.route('/json', methods=['POST'])
def json():
    req_data = request.get_json()

    language = req_data['language']
    framework = req_data['framework']
    python_version = req_data['version_info']['python']
    example = req_data['examples'][0]
    boolean_test = req_data['boolean_test']

    return {}, 200


''' json job ID
	error or pass code
	test1 correct data
	test2 error data
	status code'''


if __name__ == '__main__':
     app.run(debug=True, port=5000)
