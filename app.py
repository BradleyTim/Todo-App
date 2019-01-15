
from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)

basedir = os.path.abspath(os.path.dirname(__file__))

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'db.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Todo(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	content = db.Column(db.String(200))
	complete = db.Column(db.Boolean)

@app.route('/')
def index():
	todos = reversed(Todo.query.all())

	return render_template('index.html', todos=todos)

@app.route('/add', methods=['POST'])
def add_todo():
	todo = Todo(content=request.form['todoitem'], complete=False)
	db.session.add(todo)
	db.session.commit()
	return redirect(url_for('index'))

if __name__ == '__main__':
	app.run(debug=True)