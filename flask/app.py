# Importing Flask cladd from flask library
from flask import Flask, redirect, url_for, request

# Creating an application instance
# the argument for the constructor is the main module name
# main module name will be there in the dunder __name__
app = Flask(__name__)


# defining a route in flask using the app.route decorator
# app is out flask application obj
# / is the root of the website, like the default index.html
# greet() fn will be executed when accessing the default route
@app.route('/')
def greet():
    return 'Have a Good Day!'

@app.route('/hello')
def hello():
    return '<h1>Hello, World!</h1>'

# @app.route('/user/<name>')
# def user(name):
#     return f'<h1>Hello, {name}</h1>'

# demonstrate dynamic url building in flask
@app.route('/admin')
def welcome_admin():
    return 'Welcome admin'

@app.route('/guest/<guest>')
def hello_guest(guest):
    return f'<h1>Hello, {guest} You are our guest</h1>'

# dynamically redirect to the routes based on the user name
@app.route('/user/<name>')
def hello_user(name):
    if name == 'admin':
        return redirect(url_for('welcome_admin'))
    else:
        return redirect(url_for(f'hello_guest', guest=name))

# @app.route('/mylogin', methods=['POST'])
# def mylogin():
#     username = request.form['username']
#     password = request.form['password']
#     if username == 'abhi' and password == 'abhipass':
#         return f'Welcome {username}'
#     else:
#         return 'Username or password is not valid'

@app.route('/mylogin', methods=['GET'])
def mylogin():
    username = request.args.get('username')
    password = request.args.get('password')
    if username == 'abhi' and password == 'abhipass':
        return f'Welcome {username}'
    else:
        return 'Username or password is not valid'

# check if its the main module, then run the app
if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)