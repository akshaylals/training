from flask import Flask, render_template, request

from myformclass import NameForm

app = Flask(__name__)

app.config['SECRET_KEY'] = 'secret string'


@app.route('/', methods=['GET', 'POST'])
def wtf():
    if request.form.get('name'):
        return render_template('wtf.html', form=NameForm(), name=request.form.get('name'))
    else:
        return render_template('wtf.html', form=NameForm())