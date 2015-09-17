from flask import render_template
from my_app import app
from flask import request
from datetime import datetime
import pandas as pd


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
    #import the data
    df = pd.DataFrame.from_csv('df_all_features.csv')
    #get all of the features from the dataframe for the search day
    feat = df.loc[date2]
    coeff1 = [-3.33575407,  0.3665131 ,  0.3747563 , -0.37711144, -0.07112776,
        -1.73560827,  0.31721144, -0.9247586 ,  0.71542459, -0.10758669,
         0.24108984, -0.07855787,  0.0816439 ,  0.04022112, -0.03925997,
         0.01913135, -0.03194769, -0.05372713, -1.56868267, -0.08839249,
        -0.14908038,  0.11054076, -0.13669967, -0.31210935, -0.51587257,
        -0.43095728, -0.47385046,  0.02399595, -0.06826643,  0.05604179,
        -0.09962604, -0.0236647 , -0.20414778,  0.22855476, -0.08140042,
        -0.21506181, -0.173589  , -0.34388779,  0.18881734,  0.78362064,
        -0.34262406,  0.01573952, -0.06551674,  0.13626762, -0.23645159,
         0.45224634, -0.02358166,  0.00658083,  0.02662243, -0.19967242,
         0.27577798,  0.76978054, -2.20843292, -0.88415636,  4.46609421]


    count = 0
    crowd = 0
    for feature in feat:
        crowd += feature*coeff1[count]
        print crowd


    return render_template("output.html", date2=crowd, time1=time1)


# @app.route('/', methods=['POST'])
# def my_form_post():
#     return render_template("/output.html",
#        title = 'Home',
#         user = 'processed_text tada!!!!')
