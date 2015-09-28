from flask import render_template
from my_app import app
from flask import request
from datetime import datetime
import pandas as pd
import cPickle as pickle
from plots import *
import json


def load_classifier(fname):
   with open(fname, 'rb') as fid:
       clf = pickle.load(fid)
   return clf

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
    date1 = request.args.get('date-picker-2')
    time1 = request.args.get('ttime')

    #convert the input time to a python timestamp
    date2 = datetime.strptime(date1,"%m/%d/%Y")

    if time1 == '0':
        dates = [date2 - pd.Timedelta(days=1)]
        dates.append(date2)
    elif time1 == '1':
        dates = [date2 - pd.Timedelta(days=1)]
        dates.append(date2)
        dates.append(date2 + pd.Timedelta(days=1))
    elif time1 == '2':
        dates = [date2]
        dates.append(date2 + pd.Timedelta(days=1))
    elif time1 == '3':
        dates = [date2 - pd.Timedelta(days=2)]
        dates.append(date2 - pd.Timedelta(days=1))
        dates.append(date2)
    elif time1 == '4':
        dates = [date2 - pd.Timedelta(days=2)]
        dates.append(date2 - pd.Timedelta(days=1))
        dates.append(date2)
        dates.append(date2 + pd.Timedelta(days=1))
        dates.append(date2 + pd.Timedelta(days=2))
    elif time1 == '5':
        dates = [date2]
        dates.append(date2 + pd.Timedelta(days=1))
        dates.append(date2 + pd.Timedelta(days=2))
    elif time1 == '6':
        dates = [date2 - pd.Timedelta(days=3)]
        dates.append(date2 - pd.Timedelta(days=2))
        dates.append(date2 - pd.Timedelta(days=1))
        dates.append(date2)
    elif time1 == '7':
        dates = [date2 - pd.Timedelta(days=3)]
        dates.append(date2 - pd.Timedelta(days=2))
        dates.append(date2 - pd.Timedelta(days=1))
        dates.append(date2)
        dates.append(date2 + pd.Timedelta(days=1))
        dates.append(date2 + pd.Timedelta(days=2))
        dates.append(date2 + pd.Timedelta(days=3))
    elif time1 == '8':
        dates = [date2]
        dates.append(date2 + pd.Timedelta(days=1))
        dates.append(date2 + pd.Timedelta(days=2))
        dates.append(date2 + pd.Timedelta(days=3))
    elif time1 == '9':
        dates = [date2 - pd.Timedelta(days=7)]
        dates.append(date2 - pd.Timedelta(days=6))
        dates.append(date2 - pd.Timedelta(days=5))
        dates.append(date2 - pd.Timedelta(days=4))
        dates.append(date2 - pd.Timedelta(days=3))
        dates.append(date2 - pd.Timedelta(days=2))
        dates.append(date2 - pd.Timedelta(days=1))
        dates.append(date2)
    elif time1 == '10':
        dates = [date2 - pd.Timedelta(days=7)]
        dates.append(date2 - pd.Timedelta(days=6))
        dates.append(date2 - pd.Timedelta(days=5))
        dates.append(date2 - pd.Timedelta(days=4))
        dates.append(date2 - pd.Timedelta(days=3))
        dates.append(date2 - pd.Timedelta(days=2))
        dates.append(date2 - pd.Timedelta(days=1))
        dates.append(date2)
        dates.append(date2 + pd.Timedelta(days=1))
        dates.append(date2 + pd.Timedelta(days=2))
        dates.append(date2 + pd.Timedelta(days=3))
        dates.append(date2 + pd.Timedelta(days=4))
        dates.append(date2 + pd.Timedelta(days=5))
        dates.append(date2 + pd.Timedelta(days=6))
        dates.append(date2 + pd.Timedelta(days=7))

    elif time1 == '11':
        dates = [date2]
        dates.append(date2 + pd.Timedelta(days=1))
        dates.append(date2 + pd.Timedelta(days=2))
        dates.append(date2 + pd.Timedelta(days=3))
        dates.append(date2 + pd.Timedelta(days=4))
        dates.append(date2 + pd.Timedelta(days=5))
        dates.append(date2 + pd.Timedelta(days=6))
        dates.append(date2 + pd.Timedelta(days=7))
    elif time1 == '12':
        dates = [date2 - pd.Timedelta(days=14)]
        for i in range(-13,15):
            dates.append(date2 + pd.Timedelta(days=i))


    #import the data
    df = pd.DataFrame.from_csv('df_all_features.csv')
    mdl = load_classifier('lin_regr.pkl')

    #get all of the features from the dataframe for the search day
    feat = df.loc[dates]
    crowd = mdl.predict(feat)
    crowd_list = [round(element,0) for element in crowd]

    crowd_range = []
    for this_crowd in crowd:
        crowd_range.append([round(this_crowd - 10, 0), round(this_crowd + 10, 0)])

    date_plot = []
    for i in range(0,len(dates)):
        date_plot.append(str(dates[i])[5:10])

    return render_template("output.html", crowds=crowd_range, crowd_pred=crowd_list, dates=date_plot)


# @app.route('/', methods=['POST'])
# def my_form_post():
#     return render_template("/output.html",
#        title = 'Home',
#         user = 'processed_text tada!!!!')
