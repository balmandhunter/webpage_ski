import cPickle as pickle
import pandas as pd
import json
import web_functions

from flask import render_template
from my_app import app
from flask import request
from plots import *
from datetime import datetime


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
    try:
        time1 = int(request.args.get('ttime'))
    except:
        time1 = 0

    #convert the input time to a python timestamp, and make a list of dates
    date1 = request.args.get('date-picker-2')
    try:
        date2 = datetime.strptime(date1,"%m/%d/%Y")
    except:
        date2 = datetime(2015,11,15)
    dates = web_functions.get_dates_from_range_input(date2, time1)

    df, df_tick, mdl, df_runs = web_functions.import_data()
    crowd_range, crowd_list = web_functions.get_crowd_and_conf_interval(dates, df, mdl)
    df_runs.head()

    runs_list, days, runs_range = web_functions.get_runs_open_and_conf_interval(dates, df_runs)

    date_plot = web_functions.get_dates_for_plot(dates, days)

    tick_price1 = df_tick.loc[dates]
    tick_price = list(tick_price1.price.values)

    return render_template("output.html", crowds=crowd_range, crowd_pred=crowd_list, dates=date_plot, price=tick_price, runs_open=runs_list, runs_range=runs_range, def_date=date1)
