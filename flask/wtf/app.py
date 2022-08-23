from flask import Flask, render_template

from myformclass import NameForm

app = Flask(__name__)

app.config['SECRET_KEY'] = 'secret string'


@app.route('/')
def wtf():
    return render_template('wtf.html', form = NameForm())