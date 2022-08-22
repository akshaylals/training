from flask import Flask
import requests

API_URL = ('https://api.genderize.io/?name={}')

def send_api(name):
    try:
        data = requests.get(API_URL.format(name)).json()
    except Exception as e:
        print(e)
        data = None
    return data


app = Flask(__name__)


@app.route('/name/<name>')
def get_gender(name):
    response = send_api(name)
    if response:
        return f'Your name is {response["name"]}, your gender is {response["gender"]}'
    else:
        return 'Error'


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)