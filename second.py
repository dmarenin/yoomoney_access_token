import requests
import json
import time
from flask import Flask, request
import datetime


client_id = ''
client_secret = ''


app = Flask(__name__)


@app.errorhandler(Exception)
def handle_exception(e):
    return str(e), 500

@app.route('/', methods=['GET', 'POST'])
def index():
    code = request.args['code']

    url = f"""https://yoomoney.ru/oauth/token?code={code}&client_id={client_id}&grant_type=authorization_code&redirect_uri=http://100.74.24.55:8095&client_secret={client_secret}"""

    headers = {'Content-Type': 'application/x-www-form-urlencoded'}

    try:
        r = requests.post(url, headers)
    except:
        pass

    print(r)

    return '', 302

if __name__ == '__main__':
    HOST = '192.168.0.200'
    PORT = 8095

    app.run(HOST, PORT, threaded=True)

