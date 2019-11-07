#!/usr/bin/env python
# -*- coding:utf-8 -*-
#@Time    :    10:01  2019/11/5
#@Author  :    tb_youth
#@FileName:    FSFS.py
#@SoftWare:    PyCharm
#@Blog    :    http://blog.csdn.net/tb_youth


"""
four steps for features selection:
Fliter
Semi_weapper
Union
Voting
"""

from sklearn.model_selection import KFold
import numpy as np
import pandas as pd
import xlrd
from sklearn.cross_decomposition import PLSRegression

class FSFS:
    def __init__(self):
        self.n_components = 3
        self.pls = PLSRegression(n_components=self.n_components)
        pass

    #划分数据：划分为k份
    def split_data(self,k=10):
        path = r'C:\Users\Administrator\AppData\Local\Programs\Python\Python37\Learn-python-notes\material\科研实践\数据\data1.XlsX'
        df = pd.read_excel(path,sheet_name='Sheet1')
        #print(df.columns.values)
        #第一行，第一列
        head_list = list(df.columns.values)
        index_list = list(df.index.values)
        # print(head_list)
        # print(indeX_list)
        #自变量X，因变量y
        X = df[head_list[:-1]] #<class 'pandas.core.frame.DataFrame'>
        # print(X.shape)
        y = df[head_list[-1]] #<class 'pandas.core.series.Series'>
        # print(y.shape)
        # print(y.name)
        #将数据分为k份，k折交叉验证
        kf = KFold(n_splits=k,shuffle=True,random_state=0)
        for train_index,test_index in kf.split(X):
            # print(train_index)
            # print('+-------------------+')
            # print(test_index)
            X_train,y_train = X.values[train_index],y[train_index]
            #转换为DataFrame格式便于计算
            X_train = pd.DataFrame(X_train,index=train_index,columns=head_list[:-1])
            y_train = pd.DataFrame(y_train,index=train_index)
            print(X_train)
            print('+----------------------------------------------------------+')
            print(y_train)

            X_test,y_test = X.values[test_index],y[test_index]
            X_test = pd.DataFrame(X_test,index=test_index,columns=head_list[:-1])
            y_test = pd.DataFrame(y_test,index=test_index)
            # print(X_test)
            break

    #PLS
    def PLS(self):
        # self.pls.fit()
        pass








if __name__ =='__main__':
   f = FSFS()
   f.split_data()


