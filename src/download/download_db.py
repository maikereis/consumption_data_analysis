#!/usr/bin/env python
# coding: utf-8
import os
import json
import numpy as np 
import pandas as pd
import connector.mysql_connector as mysql_c

def drop_columns(df, columns):    
    df = df.drop(axis=1, level=0, columns=[columns])

def download_raw_db():
    #F_PATH = os.path.abspath('')
    with open('download/connector/cfg_files/database_analysis_cfg.json','r') as f:
        cfg = json.load(f)
    DB_NAME = cfg['DB_NAME']
    TB_NAME = cfg['PERSIST_TB_NAME']
    cursor = mysql_c.open_connection(DB_NAME, cfg)
    mysql_c.select_database(cursor, DB_NAME)
    rows = mysql_c.select_data(cursor, TB_NAME)
    cursor.close()
    database = pd.DataFrame(rows, columns=['id','client_id','payload','topic_path', 'date'], dtype=float)
    database.to_csv('../database/raw.csv', index=False)