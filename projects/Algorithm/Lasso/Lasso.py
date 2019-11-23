#!/usr/bin/env python
# -*- coding:utf-8 -*-
#@Time    :    11:20  2019/11/21
#@Author  :    tb_youth
#@FileName:    Lasso.py
#@SoftWare:    PyCharm
#@Blog    :    http://blog.csdn.net/tb_youth

from sklearn import linear_model
import pandas as pd
import numpy as np


def lasso(df,type=0):
    x_labels = df.columns.values
    # y_lables = df.index.values

    if type:
        x_data = df[x_labels[1:]]
        y_data = df[x_labels[0]]
    else:
        x_data = df[x_labels[0:-1]]
        y_data = df[x_labels[-1]]

    lasso_model = linear_model.Lasso(alpha=200.0,max_iter=20000)
    lasso_model.fit(x_data,y_data)

    #权重系数，为0则代表该特征剔除
    print(lasso_model.coef_)
    coef = pd.Series(lasso_model.coef_)

    #留下的特征数目
    print('count:',str(sum(coef!=0)))
    # for item in coef:
    #     if item != 0:
    #         print(item)

    #预测
    print(lasso_model.predict(x_data.values[-1,np.newaxis]))


if __name__=='__main__':
    # df = pd.read_csv(r'C:\Users\Administrator\Desktop\机器学习基本算法\线性回归以及非线性回归\longley.csv', index_col=0)
    path = r'C:\Users\Administrator\AppData\Local\Programs\Python\Python37\Learn-python-notes\material\科研实践\数据\data1.xlsx'
    df2 = pd.read_excel(path,index_col=0)
    lasso(df2)
    # print(df2)
