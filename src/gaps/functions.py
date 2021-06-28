import numpy as np
import pandas as pd
from datetime import timedelta
from itertools import groupby

def find_serie_gaps(serie):
    holes_index = []
    zipped = zip(serie.index, serie)
    holes = [ list(g) for k, g in groupby(zipped, lambda x: np.isnan(x[1])) if k]

    for sl in holes:
        data, _ = zip(*sl)
        holes_index.append(list(data))
    
    holes = np.array(holes_index, dtype=object)
    return holes

def flatten_gaps_list(holes_list):
    holes_list_flattened = list()
    for hole in holes_list:
        for hole_unit in hole:
            holes_list_flattened.append(hole_unit)
    return holes_list_flattened

def find_series_gaps(series):
    """
    Params:
        df (pd.DataFrame)

    Return:
        gaps_dict (dict): a dictionary with sparse lists of gaps index in each df column
    """

    gaps_dict = {}

    for serie in series.columns:

        gaps = find_serie_gaps(series[serie])

        gaps_dict[serie] = gaps

    return gaps_dict

def flatten_series_gaps(gaps_dict):
    """
    Params:
        df (pd.DataFrame)

    Return:
        gaps_dict (dict): a dictionary with flat lists of gaps index in each df column
    """

    gaps_flat_dict = {}
    for key in gaps_dict.keys():

        gaps = gaps_dict[key]
        gaps_flat = flatten_gaps_list(gaps)
        gaps_flat_dict[key] = gaps_flat

    return gaps_flat_dict

def _fill_gaps(df, holes, treshold, parameter=None):
    
    dt = timedelta(days=-1)

    for hole in holes:
        if (len(hole) >= treshold):  
            begin = hole[0]
            end = hole[-1]
            try:
                df.loc[begin:end]= df.loc[begin + dt : end+ dt].values
            except BaseException as err:
                print("Datafram lenght exeded")

def fill_gaps(data, holes, treshold, parameter=None):

    if isinstance(data, pd.DataFrame) & (len(data)>1):
        for col in data.columns:
            try:
                _fill_gaps(data[col], holes[col], treshold)
            except Exception as ex:
                print("Error trying to fill holes at: ", ex)

    elif isinstance(data, pd.Series) & (len(data)==1):
        _fill_holes(data, holes, treshold)