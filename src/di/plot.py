import seaborn as sns
import datetime as dt
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import matplotlib.dates as mdates
import matplotlib.ticker as ticker
from matplotlib import cm
cmap = plt.cm.Blues
from matplotlib.lines import Line2D
from matplotlib.patches import Patch

def show_di(df):
    fig, ax = plt.subplots(figsize=(12,2.5), sharex=True)

    #df_filtered = df[(df.index > "2021-03-02 00:00:00") & (df.index <= "2021-03-05 00:00:00")]
    df_filtered = df[(df.index > "2021-02-17 00:00:00") & (df.index <= "2021-03-10  00:00:00")]


    g1 = sns.lineplot(x=df_filtered.index, y=df_filtered['DI'])

    
    custom_lines = [
                    Line2D([0], [0], color='g', ls='dotted',lw=2),
                    Line2D([0], [0], color='k', ls='dotted',lw=2),
                    Line2D([0], [0], color='r', ls='dotted',lw=2)
                   ]
    ax.legend(custom_lines, 
                ['Confortável',
                'Parcialmente confortável',
                'Deconfortável'], 
                framealpha=.85,
                loc = 'lower right',
                #title= 'Intervalo de {} horas'.format(hours)
             )
    
    
    ax.set_ylabel('IDT (ºC)')
    ax.set_xlabel('Data')

    ax.xaxis.set_major_locator(ticker.AutoLocator())
    ax.xaxis.set_major_formatter(mdates.DateFormatter('%d/%m %Hh'))


    g1.axhline(24, color='green', ls='dotted', alpha=0.8)
    g1.axhline(26, color='k', ls='dotted', alpha=0.8)
    g1.axhline(28, color='r', ls='dotted', alpha=0.8)
    
    ax.xaxis.set_major_formatter(mdates.DateFormatter('%d/%m'))
    
    a = dt.datetime.strptime("2021-02-17 00:00:00", '%Y-%m-%d %H:%M:%S')
    b = dt.datetime.strptime("2021-03-10 00:00:00", '%Y-%m-%d %H:%M:%S')
    ax.set_xlim(a,b)
    sns.despine()

def plot_di_cons(df, start_date=None, stop_date=None):
    fig, ax = plt.subplots(figsize=(7,4), sharex=True)

    df_filtered = df[(df.index >= start_date) & (df.index <= stop_date)]


    
    ax2 = ax.twinx()
    g1 = sns.lineplot(x=df_filtered.index, y=df_filtered['Pwr'],ax=ax)
    g2 = sns.lineplot(x=df_filtered.index, y=df_filtered['DI'],color="red")

    
    custom_lines = [Line2D([0], [0], color=cmap(.7), lw=2),
                    Line2D([0], [0], color='r', lw=2)]
    ax.legend(custom_lines, 
                ['Potência',
                   'IDT'], 
                framealpha=1,
                loc = 'lower right',
                #title= 'Intervalo de {} horas'.format(hours)
             )
    
    
    ax.set_ylabel('Potência (W)')
    ax2.set_ylabel('IDT (ºC)')
    ax.set_xlabel('Data')

    ax.xaxis.set_major_locator(ticker.MultipleLocator(1))
    ax.xaxis.set_major_formatter(mdates.DateFormatter('%d/%m %Hh'))


    g2.axhline(24, color='green', ls='dotted')
    g2.axhline(26, color='k', ls='dotted')
    g2.axhline(28, color='r', ls='dotted')
    
    ax.xaxis.set_major_formatter(mdates.DateFormatter('%d/%m %Hh'))

def plot_di_cons2(df):
    fig, ax = plt.subplots(figsize=(14,4), sharex=True)

    #df_filtered = df[(df.index > "2021-03-02 00:00:00") & (df.index <= "2021-03-05 00:00:00")]
    df_filtered = df[(df.index > "2021-02-17 00:00:00") & (df.index <= "2021-02-28  00:00:00")]


    g1 = sns.lineplot(x=df_filtered.index, y=df_filtered['DI'],color="red")

    
    custom_lines = [Line2D([0], [0], color='r', lw=2),
                    Line2D([0], [0], color='g', ls='dotted',lw=2),
                    Line2D([0], [0], color='k', ls='dotted',lw=2),
                    Line2D([0], [0], color='r', ls='dotted',lw=2)
                   ]
    ax.legend(custom_lines, 
                ['Umidade',
                'Confortável',
                'Parcialmente confortável',
                'Deconfortável'], 
                framealpha=.85,
                loc = 'lower right',
                #title= 'Intervalo de {} horas'.format(hours)
             )
    
    
    ax.set_ylabel('IDT (ºC)')
    ax.set_xlabel('Data')

    ax.xaxis.set_major_locator(ticker.AutoLocator())
    ax.xaxis.set_major_formatter(mdates.DateFormatter('%d/%m %Hh'))


    g1.axhline(24, color='green', ls='dotted')
    g1.axhline(26, color='k', ls='dotted')
    g1.axhline(28, color='r', ls='dotted')
    
    ax.xaxis.set_major_formatter(mdates.DateFormatter('%d/%m'))
    
    a = dt.datetime.strptime("2021-02-17 00:00:00", '%Y-%m-%d %H:%M:%S')
    b = dt.datetime.strptime("2021-02-28 00:00:00", '%Y-%m-%d %H:%M:%S')
    ax.set_xlim(a,b)

def plot_di_pwr_in_interval(df, start_date, final_date):
    fig, ax = plt.subplots(figsize=(7,4), sharex=True)
    ax2 = ax.twinx()
    dataset = df[(df.index > start_date) & (df.index < final_date)]

    g1 = sns.lineplot(x=dataset.index, y=dataset['Pwr'], ax = ax)
    
    ax.fill_between(dataset.index, dataset['Pwr'].fillna(method='ffill'), alpha=0.2,hatch='/',color='C0')

    g2 = sns.lineplot(x=dataset.index, y=dataset['DI'], ax = ax2, color ='red', )
    g2.axhline(24, color='green', ls='dotted', alpha =0.8)
    '''g2.axhline(26, color='k', ls='dotted)
    g2.axhline(28, color='r', ls='dotted')'''
    
    ax.set_ylabel('Potência (W)')
    ax2.set_ylabel('IDT (ºC)')
    ax.set_xlabel('Data')
    
    cmap = plt.cm.Blues
    custom_lines = [Line2D([0], [0], color=cmap(.8), lw=2),
                    Patch(facecolor=cmap(.3), edgecolor=cmap(.8),
                         label='Color Patch'),
                    Line2D([0], [0], color='red', lw=2),
                    Line2D([0], [0], color='w', lw=2)]
    
    energy = round(dataset['Pwr'].sum()/30000,2)
    mean_pwr = round(dataset['Pwr'].mean(),2)
    mean_di = round(dataset['DI'].mean(),2)
    
    f = dataset['Pwr'] > 20
    s = dataset['Pwr'][f]
    hours = round(s.count()/30,2)
    ax.legend(custom_lines, 
              ['Potência, Média = {} W'.format(mean_pwr).replace('.',','),
               'Energia = {} kWh'.format(energy).replace('.',','),
               'IDT, Média = {} ºC'.format(mean_di).replace('.',','), 
               ], 
                framealpha=.85,
                loc = 'upper right',
                title= 'Tempo de uso {} horas'.format(hours).replace('.',','))
    

    ax.xaxis.set_major_locator(ticker.LinearLocator(4))
    ax.xaxis.set_major_formatter(mdates.DateFormatter('%d/%m %Hh')) 