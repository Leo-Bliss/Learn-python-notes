#!/usr/bin/env python
# -*- coding:utf-8 -*-
#@Time    :    2020/2/26 0026 14:12
#@Author  :    tb_youth
#@FileName:    csvToDB.py
#@SoftWare:    PyCharm
#@Blog    :    https://blog.csdn.net/tb_youth

import pandas as pd
import csv
import sqlite3

def convert(file_path):
    conn = sqlite3.connect('./db/database.db',detect_types=sqlite3.PARSE_DECLTYPES)
    # = conn.cursor()
    df = pd.read_csv(file_path)
    file_name = file_path.rsplit('/',maxsplit=1)[-1]
    file_name,_ = file_name.rsplit('.',maxsplit=1)
    print(file_name)
    #将csv中数据导入（sqlite）数据库的file_name表格
    #data_type: REAL=float)(24)
    #or: if_exists="fail","replace","append"
    df.to_sql(file_name,conn,if_exists='replace',index=False)
    sql = 'select * from test2'
    res = conn.execute(sql)
    print(len(res.fetchall()))
    conn.close()


if __name__=='__main__':
    file_path = r'./data/test2.csv'
    convert(file_path)
