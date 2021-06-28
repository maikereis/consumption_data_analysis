from matplotlib import cm
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.graph_objects as go
import matplotlib.dates as mdates
import matplotlib.ticker as ticker
 
def show_serie(df):

    fig, ax = plt.subplots(figsize=(15,3), sharex=True)
    ax.plot(df, linewidth=1)

    return ax

def show_series(dataset):
    cols = len(dataset.columns)
    height = 1.25 * cols
    space = 0.15 * cols
    fig, axes = plt.subplots(cols,1, dpi=120, figsize=(8,height))
    for i, ax in enumerate(axes.flatten()):
        data = dataset[dataset.columns[i]]
        ax.plot(data, linewidth=0.9)
        ax.set_title(dataset.columns[i], fontsize=8)
        ax.xaxis.set_ticks_position('none')
        ax.yaxis.set_ticks_position('none')
        ax.spines['top'].set_alpha(0)
        ax.tick_params(labelsize=6) 
        plt.subplots_adjust(left=None, bottom=None, right=None, top=None, wspace=None, hspace=space)
        #plt.tight_layout()

def show_hist(serie, bins=50):
    fig, ax = plt.subplots(figsize=(10,4), sharex=True)
    plt.hist(serie, bins=bins)

def show_outliers(original, outliers):
    fig, ax = plt.subplots(2,1, figsize=(15,4), sharex=True)
    ax[0].plot(original)
    ax[1].plot(original)
    ax[1].scatter(x=outliers.index, y=outliers, color='r')

def show_outliers_w_zoom(original, outliers):
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=original.index, y=original,
                    mode='lines',
                    name='Original'))
    fig.add_trace(go.Scatter(x=outliers.index, y=outliers,
                    mode='markers',
                    name='Outliers'))  
    fig.show()

def show_gaps(serie, gaps_serie, start_date=None, stop_date=None):
    fig, ax = plt.subplots(figsize=(15,4), sharex=True)
    ax.plot(serie)
    ax.plot(gaps_serie, color='r', marker='+', markersize=5)

    if (stop_date != None):
        if(start_date == None):
            ax.set_xlim(serie.index[0], stop_date)
        else:
            ax.set_xlim(start_date, stop_date)

def plot_reg_grid(df, df2=None):

    if df2 is None:
        df_wea_h = df[['T','H','DI']].resample('H').mean()
        df_wea_d = df[['T','H','DI']].resample('D').mean()
    else:
        df_wea_h = df2[['T','H','DI']].resample('H').mean()
        df_wea_d = df2[['T','H','DI']].resample('D').mean()


    df_en_h = df['Pwr'].resample('H').sum()/30000
    df_en_d = df['Pwr'].resample('D').sum()/720000


    fig, ax = plt.subplots(3,2,figsize=(10,6))

    sns.regplot(x=df_wea_h['T'], y = df_en_h, line_kws={"color": "red"}, ax=ax[0,0])
    sns.regplot(x=df_wea_d['T'], y = df_en_d, line_kws={"color": "red"}, ax=ax[0,1])
    sns.regplot(x=df_wea_h['H'], y = df_en_h, line_kws={"color": "red"}, ax=ax[1,0])
    sns.regplot(x=df_wea_d['H'], y = df_en_d, line_kws={"color": "red"}, ax=ax[1,1])
    sns.regplot(x=df_wea_h['DI'], y = df_en_h, line_kws={"color": "red"}, ax=ax[2,0])
    sns.regplot(x=df_wea_d['DI'], y = df_en_d, line_kws={"color": "red"}, ax=ax[2,1])

def show_multi_series(df):
    fig, axs = plt.subplots(2,2, figsize=(12,5))

    
    df = df[(df.index > "2021-02-17 00:00:00") & (df.index <= "2021-03-17 00:00:00")]
    sns.lineplot(x=df.index, y=df["Pwr"], linewidth =1,ax=axs[0][0])
    #sns.lineplot(x=df.index, y=df["Vrms"], ax=axs[1][0])
    #sns.lineplot(x=df.index, y=df["Irms"], ax=axs[2][0])
    #sns.lineplot(x=df.index, y=df["PF"], ax=axs[0][1])
    sns.lineplot(x=df.index, y=df["T"], linewidth =1, ax=axs[0][1])
    sns.lineplot(x=df.index, y=df["H"], linewidth =1, ax=axs[1][0])
    sns.lineplot(x=df.index, y=df["DI"], linewidth =1, ax=axs[1][1])


    axs[0][0].set_ylabel("Potência (W)")
    #axs[0][1].set_ylabel("Fator de Potência")
    #axs[1][0].set_ylabel("Tensão (V)")
    #axs[1][1].set_ylabel("Temperatura (ºC)")
    axs[0][1].set_ylabel("Temperatura (ºC)")
    axs[1][0].set_ylabel("Umidade (%)")
    axs[1][1].set_ylabel("IDT (ºC)")

    
    axs[1][0].set_xlabel('Dia')
    axs[1][1].set_xlabel('Dia')
    
    
    
    axs[0][0].xaxis.set_major_locator(ticker.AutoLocator())
    axs[0][0].xaxis.set_major_formatter(mdates.DateFormatter('%d/%m'))
    
    axs[0][1].xaxis.set_major_locator(ticker.AutoLocator())
    axs[0][1].xaxis.set_major_formatter(mdates.DateFormatter('%d/%m'))
    
    
    axs[1][0].xaxis.set_major_locator(ticker.AutoLocator())
    axs[1][0].xaxis.set_major_formatter(mdates.DateFormatter('%d/%m'))
    
    axs[1][1].xaxis.set_major_locator(ticker.AutoLocator())
    axs[1][1].xaxis.set_major_formatter(mdates.DateFormatter('%d/%m'))
    
    axs[1][0].xaxis.set_major_locator(ticker.AutoLocator())
    axs[1][0].xaxis.set_major_formatter(mdates.DateFormatter('%d/%m'))
    
    axs[0][0].xaxis.set_major_locator(ticker.AutoLocator())
    axs[0][0].xaxis.set_major_formatter(mdates.DateFormatter('%d/%m'))

    axs[1][0].tick_params(which='both', width=2)
    axs[1][0].tick_params(which='major', length=7)
    
    
    axs[1][1].xaxis.set_major_locator(ticker.AutoLocator())
    axs[1][1].xaxis.set_major_formatter(mdates.DateFormatter('%d/%m'))

    axs[1][1].tick_params(which='both', width=2)
    axs[1][1].tick_params(which='major', length=7)
    fig.align_labels()
    plt.subplots_adjust(left=None, bottom=None, right=None, top=None, wspace=None, hspace=0.5)

    
