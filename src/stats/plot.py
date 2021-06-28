import matplotlib.pyplot as plt
from statsmodels.tsa.seasonal import seasonal_decompose

from statsmodels.graphics.tsaplots import plot_acf
from statsmodels.graphics.gofplots import qqplot



def show_qqplot(serie):
    fig, ax = plt.subplots(figsize=(4,4))
    q1 = qqplot(serie, line='s', ax=ax)
    ax.set_xlabel('Quantis teóricos')
    ax.set_ylabel('Quantis de amostra')

def show_boxplot_grid(df_lst, var):
    fig, axs = plt.subplots(3,2, figsize=(7,4.5))
    
    g = sns.boxplot(data=df_lst[0][var], orient='h',ax = axs[0,0])
    g = sns.boxplot(data=df_lst[1][var], orient='h',ax = axs[0,1])
    g = sns.boxplot(data=df_lst[2][var], orient='h',ax = axs[1,0])
    g = sns.boxplot(data=df_lst[3][var], orient='h',ax = axs[1,1])
    g = sns.boxplot(data=df_lst[4][var], orient='h',ax = axs[2,0])
    g = sns.boxplot(data=df_lst[5][var], orient='h',ax = axs[2,1])
    
    

    axs[2][0].set_xlabel("Potência (W)")
    axs[2][1].set_xlabel("Potência (W)")
    
    axs[0][0].set_ylabel(df_lst[0].name)
    axs[0][1].set_ylabel(df_lst[1].name)
    axs[1][0].set_ylabel(df_lst[2].name)
    axs[1][1].set_ylabel(df_lst[3].name)
    axs[2][0].set_ylabel(df_lst[4].name)
    axs[2][1].set_ylabel(df_lst[5].name)
    plt.tight_layout()

def show_dist_grid(df):

    fig, ax = plt.subplots(2,2,figsize=(8,6))

    fig.suptitle('Histogramas', fontsize=12)
    
    ax[0,0].set_title('Temperatura')
    ax[0,0].hist(df['T'], bins=50)
    ax[0,1].set_title('Umidade')
    ax[0,1].hist(df['H'], bins=50)
    ax[1,0].set_title('Índice de Desconforto')
    ax[1,0].hist(df['DI'], bins=50)
    ax[1,1].set_title('Potência Elétrica')
    ax[1,1].hist(df['Pwr'], bins=50)
    plt.subplots_adjust(left=None, bottom=None, right=None, top=None, wspace=None, hspace=0.5)

def show_decompose(serie, period):

    res = seasonal_decompose(serie, period=period, model='additive')

    fig, ax = plt.subplots(4,1,figsize=(14,6), sharex=True)
    ax[0].plot(res.observed)
    ax[1].plot(res.trend)
    ax[2].plot(res.seasonal)
    ax[3].scatter(res.resid.index, res.resid, marker='+', s=3)



