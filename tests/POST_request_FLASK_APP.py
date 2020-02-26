from flask import Flask, request

app = Flask(__name__)


@app.route('/json', methods=['POST'])
def test_json():
	
    app.config['TESTING'] = True
    client = app.test_client()

    result = client.get('/json')
    assert '200' in result.data


