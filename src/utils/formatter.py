
import numpy as np
import pandas as pd

from datetime import timedelta
from itertools import groupby, count


G22 = 1760/(22*1000)
G47 = 1760/(47*1000)
G82 = 1760/(82*1000)


def dt_remover(df):
    indice = count()
    zipped = zip(df.index, indice)
    lst = [(date - timedelta(seconds=0.7*indice)) for date, indice in zipped]
    df.index = lst
    return df.resample('2min').mean()

def rename_columns(df):
    df.columns = [label.split('/')[1] for label in list(df.columns)]

def apply_sct_gain(df):
    variable = {'Irms','Pwr'}
    for node_name in list(set(df.columns.get_level_values(0))):
        for col in df[node_name].columns:
            el = col.split('/')
            if el[1] in variable:
                if 'R47' in col:
                    df[node_name, col] *= G47
                elif 'R82' in col:
                    df[node_name, col] *= G82
                elif 'R22' in col:
                    df[node_name, col] *= G22

def pivot_database(path, file_name):
    df_csv = pd.read_csv(path+"/"+file_name, infer_datetime_format=True)

    pvt_df = pd.pivot_table(df_csv, index=['date'], values=['payload'], columns=['client_id','topic_path'])
    pvt_df.index = pd.DatetimeIndex(pvt_df.index)

    pvt_df = pvt_df.resample('2Min').mean()

    pvt_df.sort_index(axis=1, inplace = True)

    node_id = np.array(pvt_df.columns.get_level_values(1))
    node_sens_info  = np.array(pvt_df.columns.get_level_values(2))

    header = [node_id, [info.split('/',2)[2] for info in node_sens_info]]
    header_tuple = list(zip(*header))

    multi_index = pd.MultiIndex.from_tuples(header_tuple, names=['', ''])
    pvt_df.columns = multi_index

    return pvt_df

def remove_offset(serie, threshold = 0.0, offset = 0.0):

    offsetted = ~(serie < threshold)
    serie.loc[offsetted] -= offset


def get_energy(df):
    on = df['Pwr'] > 0
    return df[on]['Pwr'].sum()/30

def get_usetime(df):

    on = df['Pwr'] > 5

    return df[on]['Pwr'].count()/30


