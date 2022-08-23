from flask import Flask, render_template
from flask_material import Material

app = Flask(__name__)
Material(app)


@app.route('/user/<name>')
def user(name):
    return render_template(
        'user.html',
        username = name,
        n = 3
    )


@app.route('/material/<name>')
def material(name):
    return render_template(
        'material.html',
        username = name,
        n = 3
    )