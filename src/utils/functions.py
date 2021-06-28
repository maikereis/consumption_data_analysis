import os
import glob
import numpy as np
import pandas as pd


def load_datasets_from_csv(directory):

    df_dict = {}
    files = glob.glob(directory+'/*.csv', recursive=True)

    for f in files:

        f_name = os.path.basename(f)
        df_name = os.path.basename(f).replace('.csv','')

        df = pd.read_csv(directory+'/'+f_name, index_col=0, parse_dates=True)#
        df_dict[df_name] = df

    return df_dict

def clean_folder(folder_path, files):

    files = glob.glob(folder_path+'/'+files, recursive=True)

    for f in files:
        os.remove(f)

def lists_to_dict(lst_k, lst_v, order=False):
    data_dict = dict(zip(lst_k, lst_v))
    if order:
        return dict(sorted(data_dict.items(), key=lambda item: item[1], reverse=True))
    else:
        return data_dict