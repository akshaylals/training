from flask import Flask, render_template, request
from werkzeug.utils import secure_filename

from myformclass import NameForm

app = Flask(__name__)

app.config['SECRET_KEY'] = 'secret string'


@app.route('/', methods=['GET', 'POST'])
def wtf():
    if request.form.get('name'):
        return render_template('wtf.html', form=NameForm(), name=request.form.get('name'))
    else:
        return render_template('wtf.html', form=NameForm())


@app.route('/enquiry', methods=['GET', 'POST'])
def enquiry():
    form = NameForm()
    name = None
    if form.validate_on_submit():
        name = form.name.data
        form.name.data = ''
        filename = secure_filename(form.filename.data.filename)
        form.filename.data.save('uploads/' + filename)
        
    return render_template('wtf.html', form=form, name=name)