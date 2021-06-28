import mysql_connector
import os
import datetime
import json
from mysql_connector import open_connection, create_database, create_table, select_database, insert_data
dir_path = os.path.dirname(os.path.realpath(__file__))

with open(dir_path + '/cfg_files/'+'database_cfg.json', 'r') as f:
    cfg = json.load(f)

DB_NAME = cfg['DB_NAME']
TB_NAME = cfg['USER_TB_NAME']

cursor = open_connection(DB_NAME, cfg)
select_database(cursor, DB_NAME)
create_table(cursor, TB_NAME)


def add_user(id, username, password_hash, salt, is_superuser):

    data = {'id': id,
            'username': username,
            'password': password_hash,
            'salt': salt,
            'is_superuser': is_superuser,
            'created': datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            }
    insert_data(cursor, TB_NAME, data)
