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
import math
# import xlrd
from sklearn.cross_decomposition import PLSRegression

class FSFS:
    def __init__(self,path):
        self.n_components = 3
        self.pls = PLSRegression(n_components=self.n_components,scale=True)
        self.path = path
        pass

    def run(self,k=10):
        df = pd.read_excel(self.path,sheet_name='Sheet1',index_col=0)

        #print(df.columns.values)
        #第一行，第一列
        header_list = list(df.columns.values)
        index_list = list(df.index.values)
        # print(header_list)
        # print(indeX_list)
        #自变量X，因变量y
        X = df[header_list[:-1]] #<class 'pandas.core.frame.DataFrame'>
        # print(X.shape)
        y = df[header_list[-1]] #<class 'pandas.core.series.Series'>
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
            X_train = pd.DataFrame(X_train,index=train_index,columns=header_list[:-1])
            y_train = pd.DataFrame(y_train.values,index=train_index,columns=[header_list[-1]])
            X_test,y_test = X.values[test_index],y[test_index]
            X_test = pd.DataFrame(X_test,index=test_index,columns=header_list[:-1])
            y_test = pd.DataFrame(y_test.values,index=test_index,columns=[header_list[-1]])

            #训练得到相关参数，即得到拟合方程
            self.pls.fit(X_train, y_train)
            #代入测试集中的自变量得到预测的因变量
            y_test_predict = self.pls.predict(X_test)

            # print(y_test_predict)
            # print(type(y_test_predict))
            # print(y_test)
            # print(type(y_test.values))

            #得到未开始特征选择的RMSE值
            old_RMSE = self.get_RMSE(y_test_predict,y_test)
            print(old_RMSE)

            # Filter

            break

    #RMSE
    def get_RMSE(self,y_predict,y_test):
        MSE = np.mean((y_test - y_predict) ** 2)
        RMSE = math.sqrt(MSE)
        return RMSE

    #PLS
    def PLS(self):
        pass




if __name__ =='__main__':
   path = r'C:\Users\Administrator\AppData\Local\Programs\Python\Python37\Learn-python-notes\material\科研实践\数据\data1.xlsx'
   f = FSFS(path)
   f.run()

