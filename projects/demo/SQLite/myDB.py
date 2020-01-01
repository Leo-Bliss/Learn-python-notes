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


def update(sql,*args):
    conn = sqlite3.connect('./db/database.db', detect_types=sqlite3.PARSE_DECLTYPES)
    cursor = conn.cursor()
    try:
        cursor.execute(sql,*args)
    except Exception as e:
        print(e)
        pass
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
    # update(sql)
    # # sql = "select * from user order by 1 ASC "
    # # query(sql)

    # # 删除icon表
    # sql = "drop table userIcon"
    # update(sql)

    # # 建icon表
    # sql = "create table userIcon(user_id varchar (50) primary key,file_name varchar (50) ,file_type varchar (10),content BLOB)"
    # update(sql)

    # 查看数据库字段
    sql = "PRAGMA table_info(userIcon)"
    res = query(sql)
    print(res)

    import base64
    path = "./image/avatar.jpg"

    # 导入图片
    with open("{}".format(path),"rb") as f:
        content = base64.b64encode(f.read())
        dir,file = path.rsplit('/',maxsplit=1)
        file_name,file_type = file.rsplit('.',maxsplit=1)
        print(file_name,file_type)

        # file_id = '2'
        # sql = "insert into userIcon values(?,?,?,?)"
        # para = (file_id,file_name,file_type,content)
        # update(sql,para)

    # #删除数据
    # sql = "delete from userIcon where user_id = '2'"
    # update(sql)

    sql = "select * from userIcon"
    res = query(sql)[0]

    #导出图片
    with open("./image/{}{}.{}".format(res[1],res[0],res[2]),"wb") as f:
        f.write(base64.b64decode(res[-1]))








