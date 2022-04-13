from email.policy import default
from flask import *
import json, time

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    dataset = {'page': 'Home', 'Message': 'successfully loaded the home page' , 'Timestamp': time.time()}
    jsondump = json.dumps(dataset)
    return jsondump

@app.route('/user/', methods=['GET'])
def request_shreya():

    user_query = str(request.args.get('user'))

    dataset = {'page': 'request', 'Message': f'successfully loaded the request for {user_query} pages', 'Timestamp': time.time()}
    jsondump = json.dumps(dataset)

    return jsondump


if __name__ == '__main__':
    app.run(port=2000)