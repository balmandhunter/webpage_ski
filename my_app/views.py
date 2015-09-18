from flask import render_template
from my_app import app
from flask import request
from datetime import datetime
import pandas as pd
import cPickle as pickle
from plots import *

def load_classifier(fname):
   # load it again
   with open(fname, 'rb') as fid:
       clf = pickle.load(fid)
       #clf = joblib.load(fname)

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
    print date1

    time1 = request.args.get('ttime')

    #convert the input time to a python timestamp
    date2 = datetime.strptime(date1,"%m/%d/%Y")
    #import the data
    df = pd.DataFrame.from_csv('df_all_features.csv')
    mdl = load_classifier('lin_regr.pkl')

    #get all of the features from the dataframe for the search day
    feat = df.loc[date2]
    crowd = mdl.predict(feat[1:])

    pic1 = make_bar_chart(crowd, 'Crowd', date2)
    return render_template("output.html", date2=crowd, time1=time1, pic1=pic1)


# @app.route('/', methods=['POST'])
# def my_form_post():
#     return render_template("/output.html",
#        title = 'Home',
#         user = 'processed_text tada!!!!')
