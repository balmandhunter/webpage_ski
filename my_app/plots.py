import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats
import numpy as np

from datetime import datetime
import StringIO
import random
import os

from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
from matplotlib.dates import DateFormatter
from flask import make_response


def plot_params():
    size = 18
    a = plt.rc('xtick', labelsize = size)
    b = plt.rc('ytick', labelsize = size)
    return a, b, plt.gca()

def plot_ticket_sales(df):
    plt.figure(facecolor='w', figsize = (15,20))
    a, b, axes, label_size = plot_params()

    ax1 = plt.subplot(311)
    df['tickets'].plot(marker = '.',linestyle = '-', label = 'Total Tickets Sold')
    plt.ylabel('Number of Tickets', size = label_size)
    plt.legend(fontsize = label_size)
    plt.xlabel('Date', size = label_size)

    ax2 = plt.subplot(312)
    df['is_CO'].plot(marker = '.',linestyle = '-', label = 'Sales to CO Residents')
    plt.ylabel('Number of Tickets', size = label_size)
    plt.legend(fontsize = label_size)
    plt.xlabel('Date', size = label_size)

    ax3 = plt.subplot(313)
    df['not_CO'].plot(marker = '.',linestyle = '-', label = 'Sales to Out-of-State Visitors')
    plt.ylabel('Number of Tickets', size = label_size)
    plt.legend(fontsize = label_size)
    plt.xlabel('Date', size = label_size)


def make_correlation_plot(df):
    f, ax = plt.subplots(figsize=(12, 12))
    sns.corrplot(df, annot=True, sig_stars=False,
             diag_names=False, ax=ax)


def plot_two_lines(df, col1, col2, y_title1, y_title2, xlim):
	plt.figure(facecolor='w', figsize = (15,10))
	a, b, axes, label_size = plot_params()

	df[col1].plot(marker = 'o',linestyle = '-', label = y_title1, xlim = xlim)
	df[col2].plot(marker = 'o',linestyle = '-', label = y_title2, xlim = xlim)
	plt.legend(fontsize = label_size)


def plot_one_line(df, col1, y_title1, xlim):
	plt.figure(facecolor='w', figsize = (15,10))
	a, b, axes, label_size = plot_params()

	df[col1].plot(marker = 'o',linestyle = '-', label = y_title1, xlim = xlim)
	plt.legend(fontsize = label_size)


def plot_six_lines(df, col1, col2, col3, col4, col5, col6, y_title1, y_title2, y_title3, y_title4, y_title5, y_title6, xlim):
    plt.figure(facecolor='w', figsize = (15,10))
    a, b, axes, label_size = plot_params()

    df[col1].plot(marker = 'o',linestyle = '-', label = y_title1, xlim = xlim)
    df[col2].plot(marker = 'o',linestyle = '-', label = y_title2, xlim = xlim)
    df[col3].plot(marker = 'o',linestyle = '-', label = y_title3, xlim = xlim)
    df[col4].plot(marker = 'o',linestyle = '-', label = y_title4, xlim = xlim)
    df[col5].plot(marker = 'o',linestyle = '-', label = y_title5, xlim = xlim)
    df[col6].plot(marker = 'o',linestyle = '-', label = y_title6, xlim = xlim)
    plt.legend(fontsize = label_size)


def plot_hist(values, title, ):
    plt.figure(figsize = (10,5), facecolor='w')
    a, b, axes, label_size = plot_params()
    h = sorted(values)
    fit = stats.norm.pdf(h, np.mean(h), np.std(h))
    plt.plot(h, fit, '-o')
    plt.title(title, size = label_size)
    min1 = min(values)
    max1 = max(values)
    plt.hist(h)
    plt.show()


def make_bar_chart(crowd, y_label, dates):
    a, b, label_size = plot_params()
    N = len(crowd)

    ind = np.arange(N)  # the x locations for the groups
    width = 0.35      # the width of the bars

    fig, ax = plt.subplots(figsize=(7, 4), facecolor='white', frameon=False)
    #plt.box(on='off')
    rects1 = ax.bar(ind, crowd, width, yerr = 1109, color='#bdbdbd', edgecolor = "none")

    # add some text for labels, title and axes ticks
    ax.set_ylabel(y_label, size = 18)
    ax.set_xlabel("Date", size = 18)
    ax.set_title(' ')
    ax.set_xticks(ind + width/2)
    ax.margins(0.1,0)
    tick_labels = dates
    plt.xticks(rotation=70)
    ax.set_xticklabels(tick_labels, size = 10)
    ax.grid(False)
    plt.ylim([0,max(crowd)+ 0.2])

    plt.savefig('my_app/static/temp/fig1.png')
    plt.close()
    return os.path.split('my_app/static/temp/fig1.png')[1]




if __name__ == "__main__":
    import sys
    fib(int(sys.argv[1]))
