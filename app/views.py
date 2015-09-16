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

   


# @app.route('/', methods=['POST'])
# def addRegion():
#     return render_template("index.html",
#        title = 'Home',
#        user = 'processed_text tada!!!!')


@app.route('/', methods=['POST'])
def my_form_post():
    return render_template("/output.html",
       title = 'Home',
        user = 'processed_text tada!!!!')


