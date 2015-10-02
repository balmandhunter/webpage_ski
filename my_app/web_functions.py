import cPickle as pickle
import datetime
import pandas as pd

from flask import render_template
from my_app import app
from flask import request


min_date = datetime.datetime(2015, 11, 15)
max_date = datetime.datetime(2016, 4, 26)


deltas = ((1, 0),
          (1, 1),
          (0, 1),
          (2, 0),
          (2, 2),
          (0, 2),
          (3, 0),
          (3, 3),
          (0, 3),
          (7, 0),
          (7, 7),
          (0, 7),
          (14, 14))


def get_dates_from_range_input(date2, time1):
    delta_begin = datetime.timedelta(deltas[time1][0])
    delta_end = datetime.timedelta(deltas[time1][1])
    date_begin = max(min_date, date2 - delta_begin)
    date_end = min(max_date, date2 + delta_end)
    days = (date_end - date_begin).days + 1
    return [date_begin + datetime.timedelta(d) for d in range(days)]


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


def get_runs_open_and_conf_interval(dates, df_runs):
    #get all of the features from the dataframe for the search day
    runs_list = list(df_runs.loc[dates].pred.values)
    runs_list = [round(run,0) for run in runs_list]

    runs_range = []
    for this_run in runs_list:
        runs_range.append([this_run - 5, this_run + 5])

    days = []
    for date in dates:
        if df_runs.loc[date].day_of_week == 0:
            days.append('Mon:')
        elif df_runs.loc[date].day_of_week == 1:
            days.append('Tues:')
        elif df_runs.loc[date].day_of_week == 2:
            days.append('Wed:')
        elif df_runs.loc[date].day_of_week == 3:
            days.append('Thurs:')
        elif df_runs.loc[date].day_of_week == 4:
            days.append('Fri:')
        elif df_runs.loc[date].day_of_week == 5:
            days.append('Sat:')
        elif df_runs.loc[date].day_of_week == 6:
            days.append('Sun:')
        else:
            days.append('error')
    return runs_list, days, runs_range


def load_classifier(fname):
    with open(fname, 'rb') as fid:
       clf = pickle.load(fid)
    return clf


def import_data():
    df = pd.DataFrame.from_csv('df_all_features.csv')
    df_tick = pd.DataFrame.from_csv('lift_tickets.csv')
    df_runs = pd.DataFrame.from_csv('df_runs_open.csv')
    mdl = load_classifier('lin_regr.pkl')
    return df, df_tick, mdl, df_runs
