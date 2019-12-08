#!/usr/bin/env python
# -*- coding:utf-8 -*-
#@Time    :    2019/12/8 0008 22:58
#@Author  :    tb_youth
#@FileName:    myDB.py
#@SoftWare:    PyCharm
#@Blog    :    https://blog.csdn.net/tb_youth

'''
操作SQLite数据库

'''


from PyQt5.QtSql import QSqlDatabase,QSqlQuery
import sqlite3

def createDB():
    db = QSqlDatabase.addDatabase('QSQLITE')
    #指定SQLite数据库的文件名
    db.setDatabaseName('./db/database.db')
    if not db.open():
        print('无法建立与数据库的连接')
        return False
    query = QSqlQuery()
    sql = 'create table user(id int primary key,name varchar(10),age int,adress varchar(50),tel varchar(20))'
    query.exec(sql)
    db.close()
    return True


def updata(sql):
    conn = sqlite3.connect('./db/database.db', detect_types=sqlite3.PARSE_DECLTYPES)
    cursor = conn.cursor()
    cursor.execute(sql)
    conn.commit()
    conn.close()

def query(sql):
    conn = sqlite3.connect('./db/database.db', detect_types=sqlite3.PARSE_DECLTYPES)
    cursor = conn.cursor()
    cursor.execute(sql)
    data = cursor.fetchall()
    print(data)
    conn.close()
    return data


if __name__=='__main__':
    # createDB()
    # sql = "insert into user values(4,'John',19,'Aasjdah','ashhajjds')"
    # updata(sql)
    sql = "select * from user order by 1 ASC "
    query(sql)




