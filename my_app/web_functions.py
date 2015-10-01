from flask import render_template
import cPickle as pickle
from my_app import app
from flask import request
from datetime import datetime
import pandas as pd

def get_dates_from_range_input(date2, time1):
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
    else:
        dates = [date2 - pd.Timedelta(days=1)]
        dates.append(date2)

    return dates


def get_dates_for_plot(dates, days):
    date_plot = []
    for i in range(0,len(dates)):
        date_plot.append(str(days[i]) + ' ' + str(dates[i])[5:10])

    return date_plot


def get_crowd_and_conf_interval(dates, df, mdl):
    #get all of the features from the dataframe for the search day
    feat = df.loc[dates]
    crowd = mdl.predict(feat)
    crowd_list = [round(element,0) for element in crowd]

    crowd_range = []
    for this_crowd in crowd:
        crowd_range.append([round(this_crowd - 10, 0), round(this_crowd + 10, 0)])
    return crowd_range, crowd_list


def get_runs_open_and_conf_interval(dates, df_runs, rfr_mdl):
    #get all of the features from the dataframe for the search day
    runs_list = list(df_runs.loc[dates].pred.values)
    runs_list = [round(run,0) for run in runs_list]

    days = []
    for date in dates:
        if df_runs.loc[date].day_of_week == 0:
            days.append('Monday')
        elif df_runs.loc[date].day_of_week == 1:
            days.append('Tuesday')
        elif df_runs.loc[date].day_of_week == 2:
            days.append('Wednesday')
        elif df_runs.loc[date].day_of_week == 3:
            days.append('Thursday')
        elif df_runs.loc[date].day_of_week == 4:
            days.append('Friday')
        elif df_runs.loc[date].day_of_week == 5:
            days.append('Saturday')
        elif df_runs.loc[date].day_of_week == 6:
            days.append('Sunday')
        else:
            days.append('error')
    # runs_range = []
    # for this_run in runs:
    #     runs_range.append([round(this_run - 10, 0), round(this_run + 10, 0)])
    return runs_list, days


def load_classifier(fname):
    with open(fname, 'rb') as fid:
       clf = pickle.load(fid)
    return clf


def import_data():
    df = pd.DataFrame.from_csv('df_all_features.csv')
    df_tick = pd.DataFrame.from_csv('lift_tickets.csv')
    df_runs = pd.DataFrame.from_csv('df_runs_open.csv')
    mdl = load_classifier('lin_regr.pkl')
    rfr_mdl = load_classifier('rfr.pkl')
    return df, df_tick, mdl, rfr_mdl, df_runs
