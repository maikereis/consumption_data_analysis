from matplotlib import cm
import matplotlib.pyplot as plt
import seaborn as sns

def show_gaps(serie, gaps_serie, start_date=None, stop_date=None):
    """
    This function show a time series and his missing values at 0 with red color

    Params:
        serie : pd.Series or array like
        gaps_serie: pd.Series or array like
        start_date = date.datetime.Timestamp
        stop_date = date.datetime.Timestamp

    """
    fig, ax = plt.subplots(figsize=(15,3), sharex=True)
    ax.plot(serie, linewidth=1)
    ax.plot(gaps_serie, color='r', marker='+', markersize=5)
    ax.set_title("Gaps", fontsize=12)
    ax.xaxis.set_ticks_position('none')
    ax.yaxis.set_ticks_position('none')
    ax.spines['top'].set_alpha(0)
    ax.tick_params(labelsize=10) 
    plt.subplots_adjust(left=None, bottom=None, right=None, top=None, wspace=None, hspace=0.6)

    if (stop_date != None):
        if(start_date == None):
            ax.set_xlim(serie.index[0], stop_date)
        else:
            ax.set_xlim(start_date, stop_date)
