from flask import render_template
from app import app
from flask import request


@app.route('/')
def index():
   user = '' # fake user
   return render_template("index.html",
       title = 'Home',
       user = user)



@app.route('/output')
def output():
    date1 = request.args.get('date-picker-2')
    time1 = request.args.get('ttime')
    print time1
    return render_template("output.html", date1=date1, time1=time1)


# @app.route('/', methods=['POST'])
# def my_form_post():
#     return render_template("/output.html",
#        title = 'Home',
#         user = 'processed_text tada!!!!')



