import mysql_connector
import os
import datetime
import json
from mysql_connector import open_connection, create_database, create_table, select_database, insert_data
dir_path = os.path.dirname(os.path.realpath(__file__))

with open(dir_path + '/cfg_files/'+'database_cfg.json', 'r') as f:
    cfg = json.load(f)

DB_NAME = cfg['DB_NAME']
TB_NAME = cfg['ACL_TB_NAME']

cursor = open_connection(DB_NAME, cfg)
select_database(cursor, DB_NAME)
create_table(cursor, TB_NAME)


def authorize_user(id, allow, ipaddr, username, clientid, access, topic):

    data = {'id': id,
            'allow': allow,
            'ipaddr': ipaddr,
            'username': username,
            'clientid': clientid,
            'access': access,
            'topic': topic,
            }
    insert_data(cursor, TB_NAME, data)
    