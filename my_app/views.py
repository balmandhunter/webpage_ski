from flask import render_template
import cPickle as pickle
from my_app import app
from flask import request
from datetime import datetime
import pandas as pd
from plots import *
import json
from web_functions import *


#tell flask which html file to open when on the homepage (www.skiinsolitude.com)
@app.route('/')
def index():
   user = '' # fake user
   return render_template("index.html",
       title = 'Home',
       user = user)


#tell flask which html file to open when the extension is skiinsolitude/output
@app.route('/output')
def output():
    #get user inputs
    date1 = request.args.get('date-picker-2')
    time1 = request.args.get('ttime')

    #convert the input time to a python timestamp, and make a list of dates
    date2 = datetime.strptime(date1,"%m/%d/%Y")
    dates = get_dates_from_range_input(date2, time1)

    df, df_tick, mdl, df_runs = import_data()
    crowd_range, crowd_list = get_crowd_and_conf_interval(dates, df, mdl)
    df_runs.head()

    runs_list, days, runs_range = get_runs_open_and_conf_interval(dates, df_runs)

    date_plot = get_dates_for_plot(dates, days)

    tick_price1 = df_tick.loc[dates]
    tick_price = list(tick_price1.price.values)

    return render_template("output.html", crowds=crowd_range, crowd_pred=crowd_list, dates=date_plot, price=tick_price, runs_open=runs_list, runs_range=runs_range)


# @app.route('/', methods=['POST'])
# def my_form_post():
#     return render_template("/output.html",
#        title = 'Home',
#         user = 'processed_text tada!!!!')
