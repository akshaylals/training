from flask import Flask, render_template, redirect, url_for, request, flash
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Declaring the database uri as the key into flask config object
# mssql+pyodbc://server/dbname?driver=driver
app.config['SQLALCHEMY_DATABASE_URI'] = 'mssql+pyodbc://DESKTOP-4GIE4U2\SQLEXPRESS01/empdb?driver=SQL+Server+Native+Client+11.0'
# track modification key to false to optimize memory
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


# set the secret key for the forms 
app.config['SECRET_KEY'] = 'my secret key'

# instantiate the db object
db = SQLAlchemy(app)

# create a class for the model. Class name will be table name and attributes will be columns
class Employees(db.Model):
    id = db.Column('employee_id', db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    salary = db.Column(db.Float(50))
    age = db.Column(db.String(200))

    # define thje constructor
    def __init__(self, name, salary, age) -> None:
        self.name = name
        self.salary = salary
        self.age = age


db.create_all()


@app.route('/add', methods=['GET', 'POST'])
def addEmployee():
    if request.method == 'POST':
        if not request.form['name'] or not request.form['salary'] or not request.form['age']:
            flash('Please enter all the fields', 'error')
            return redirect(url_for('addEmployee'))
        else:
            employee = Employees(request.form['name'], request.form['salary'], request.form['age'])
            db.session.add(employee)
            db.session.commit()
            return redirect(url_for('listEmployees'))
    else:
        return render_template('add.html')

@app.route('/')
def listEmployees():
    return render_template(
        'list.html',
        employees=Employees.query.all()
    )


if __name__ == '__main__':
    app.run(debug=True)