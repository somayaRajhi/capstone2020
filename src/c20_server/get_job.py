from flask import Flask

app = Flask(__name__)


@app.route('/')
def get_job():
    return {
        "docketId": "CMS-2014-0115"
    }




