from flask import Flask

app = Flask(__name__)


@app.route('/')
def get_job():
    return {
        "docketId": "CMS-2014-0115"
    }


@app.route('/job/<docketId>')
def get_task(docketId):
    if len(docketId) == 0:
        return {"Error": "URL not found"}
    return {"docketId": docketId}


@app.route('/request/<username>')
def client_username_validation(username):
    if username != 'CMS':
        return {"Error": "Access Denied"}
    return {"Success": "Access Granted"}


