import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.ticker import FuncFormatter
from matplotlib import cm
cmap = plt.cm.Blues




def change_width(ax, new_value, orient='v') :
    for patch in ax.patches :

        if orient == 'v':
            current_width = patch.get_height()
        else:
            current_width = patch.get_width()

        diff = current_width - new_value
        
        if orient == 'v':
            patch.set_height(new_value)
            patch.set_y(patch.get_y() + diff * .5)
        else:
            patch.set_width(new_value)
            patch.set_x(patch.get_x() + diff * .5)

  

def plot_horizontal_bars(data_dict, h, l, unit='MU', scale_xaxis=None, bar_size=0.8):
    cm = 1/2.54
    if not isinstance(data_dict,dict):
        print("Param error!")
        return

    fig, ax = plt.subplots(figsize=(h, l), sharex=True)


    total = sum(data_dict.values())

    cmaps_lst = []
    for v in data_dict.values():
        cmaps_lst.append(cmap((v/total)+0.4))
    


    g = sns.barplot(x=list(data_dict.values()), y=list(data_dict.keys()), ax = ax,
        palette=cmaps_lst, saturation=.9, edgecolor="w", linewidth=1, dodge=True)
        
    if scale_xaxis != None:
        g.get_xaxis().set_major_formatter(FuncFormatter(lambda x, p: format(int(x*scale_xaxis), ',')))

                
    # remove axes lines
    sns.despine(fig=None, ax=None, top=False, right=True, left=True, 
        bottom=True, offset=None, trim=False)
    #put x-axis on top
    ax.xaxis.tick_top()
    #remove background grids
    ax.grid(False)
    ax.set_xlabel(unit, loc='center', labelpad=12)
    ax.xaxis.set_label_position('top') 
    g.tick_params(bottom=False, left=False)  # remove the ticks

    change_width(ax, bar_size, 'v')
    ax.set_xlabel('')
    sns.set_style("darkgrid", {"axes.facecolor": ".90"})
    ax.grid(color='w')
    ax.set_axisbelow(True)
