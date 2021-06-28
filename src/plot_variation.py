
import numpy as np
import datetime as dt
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib.dates as mdates
import matplotlib.ticker as ticker


from matplotlib import cm
cmap = plt.cm.Blues

from matplotlib.lines import Line2D
from matplotlib.patches import Patch

def calc_1_grau_func(value,Y, X):
    m = (Y[-1] - Y[0]) / (X[-1] - X[0])
    y = m*value - m*X[0] + Y[0]
    return y


def plot_t_h_curves_info(df, start_date, final_date):
    fig, ax = plt.subplots(figsize=(7,4), sharex=True)
    ax2 = ax.twinx()

    df_filtered = df[(df.index > start_date) & (df.index <= final_date)]

    ## Define variables to workon
    t = df_filtered['T'].copy()
    h = df_filtered['H'].copy()
    di = df_filtered['DI'].copy()
    
    ## Graphics
    gt = sns.lineplot(x=t.index, y=t, ax= ax)
    gh = sns.lineplot(x=h.index, y=h, ax= ax2, color='r')
    

    ## Custom legendds
    custom_lines = [Line2D([0], [0], color=cmap(.7), lw=2),
                    Line2D([0], [0], color='r', lw=2)]

    ax.legend(custom_lines, 
                ['Temperatura','Umidade'], framealpha=.85,loc = 'lower right')
    
    ## Labels
    ax.set_ylabel("Temperatura (ºC)")
    ax2.set_ylabel("Umidade (%)")
    ax.set_xlabel("Hora")

    ## Set number of ticks
    ax.xaxis.set_major_locator(ticker.LinearLocator(5))
    ax.xaxis.set_major_formatter(mdates.DateFormatter('%d/%m %Hh'))
    
    ## Calculate relationship between AXIS 
    T_yaxis = ax.yaxis.get_ticklocs()
    H_yaxis = ax2.yaxis.get_ticklocs()

    t1 = t.idxmin()
    y_t1 = t[t1]
    print(y_t1)
    t2 = t1 + dt.timedelta(hours = 2)

    y_t = t[t2]
    y_h = h[t2]
    
    s = calc_1_grau_func( y_h , list(T_yaxis), list(H_yaxis))

    ## Switch off momento text

    ax.annotate('Momento em que\no ar-condicionado\nfoi desligado', xy=(t1, y_t1+0.5), xytext=(-50, 150), 
            textcoords='offset points', arrowprops=dict(arrowstyle='->'))
    
    ## Vertical dotted line
    ax.plot([t2, t2], [y_t, s], color='k', alpha=0.6,linewidth=2.0, linestyle="dotted")

    ## Black points 
    ax.scatter([t2], [y_t], 30, color='k')
    ax2.scatter([t2], [y_h], 30, color='k')

    ## Text next black points
    ax.annotate(r'T = {:.2f} ºC'.format(y_t).replace('.',','),
             xy=(t2, y_t), xycoords='data',
             xytext=(20, -40), textcoords='offset points', fontsize=12,
             arrowprops=dict(arrowstyle="->",shrinkA=0, shrinkB=10,  connectionstyle="arc3,rad=.3"))
    
    ax2.annotate(r'RH = {:.2f} %'.format(y_h).replace('.',','),
             xy=(t2, y_h), xycoords='data',
             xytext=(20, -20), textcoords='offset points', fontsize=12,
             arrowprops=dict(arrowstyle="->",shrinkA=0, shrinkB=10,  connectionstyle="arc3,rad=.2"))