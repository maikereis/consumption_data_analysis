import numpy as np
import pandas as pd


def append_di_column(df, temp_df=None, hum_df=None):
    if temp_df is None:
        temp_df = df['T']

    if hum_df is None:
        hum_df = df['H']
        
    df['DI'] = df.apply(lambda x: x['T']-0.55*(1-0.01*x['H'])*(x['T']-14.5), axis=1)

def append_di_category(df):
    df_di = df['DI']

    conf = df_di <=24
    pconf = (df_di > 24) & (df_di < 26)
    uconf = (df_di >= 26) & (df_di < 28)
    vuconf = (df_di) >= 28
    df['DI_class'] = 0
    df.loc[conf, 'DI_class'] = 1
    df.loc[pconf, 'DI_class'] = 2
    df.loc[uconf, 'DI_class'] = 3
    df.loc[vuconf, 'DI_class'] = 4

def get_cons_by_di_class(df):

    conf =  df['DI_class'] == 1
    pconf = df['DI_class'] == 2
    uconf =  df['DI_class'] == 3
    vuconf = df['DI_class'] == 4

    cons_conf = df.loc[conf, 'Pwr'].sum()/30000
    cons_pconf = df.loc[pconf, 'Pwr'].sum()/30000
    cons_uconf = df.loc[uconf, 'Pwr'].sum()/30000
    cons_vuconf = df.loc[vuconf, 'Pwr'].sum()/30000
    
    ttl = cons_conf + cons_pconf + cons_uconf + cons_vuconf
    return ttl, cons_conf,cons_pconf, cons_uconf, cons_vuconf