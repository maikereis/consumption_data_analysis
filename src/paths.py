import os
import pandas as pd

import sys
#sys.path.append('../')

# Get current working directory (cwd)
#cwd = data_processing#os.getcwd()
  
cwd = os.path.dirname(os.path.abspath(__file__))
# Points to parent directory
ROOT_DIR = os.path.abspath(os.path.join(cwd, os.pardir))
DB_DIR = os.path.join(ROOT_DIR, 'database')
FMTD_DB_DIR = os.path.join(DB_DIR, 'formatted')
OFFSTD_DB_DIR = os.path.join(DB_DIR, 'offsetted')
FLTRD_DB_DIR = os.path.join(DB_DIR, 'filtered')
FLLD_DB_DIR = os.path.join(DB_DIR, 'filled')
PRE_FMTD_DB_DIR = os.path.join(DB_DIR, 'pre_formatted')
FXD_DB_DIR = os.path.join(DB_DIR, 'fixed')
RAW_DB_DIR = os.path.join(DB_DIR, 'raw')


PVTDB = '/pivoted.csv'



if __name__ == "__main__":
    print('\n')
    print("Folder path of this file   :",os.path.dirname(os.path.abspath(__file__)))
    print("Folder path of root dir    :",ROOT_DIR)

    print("Folder path of 'database'  :",DB_DIR)
    print("Folder path of 'raw'       :",RAW_DB_DIR)

    print("Folder path of 'pre fmtd'  :",PRE_FMTD_DB_DIR)
    print("Folder path of 'formated'  :",FMTD_DB_DIR)

    print("Folder path of 'fixed'     :",FXD_DB_DIR)
    print("Folder path of 'offsetted' :",OFFSTD_DB_DIR)

    print("Folder path of 'filtered'  :",FLTRD_DB_DIR)
    print("Folder path of 'filled'    :",FLLD_DB_DIR)

    print('\n')
