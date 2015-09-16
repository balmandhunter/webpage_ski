from flask import render_template
from app import app
from flask import request


@app.route('/')
@app.route('/index')
def index():
   user = '' # fake user
   return render_template("index.html",
       title = 'Home',
       user = user)


@app.route('/your_method_name', methods=['POST'])
def addRegion():
    return render_template("index.html",
       title = 'Home',
       user = 'tada!!!!')


@app.route('/<x>/<y>')
def maths(x,y):
	sum = int(x)+int(y)
	return render_template("index.html",
       title = 'Home',
       user = 'tada!!!!')

