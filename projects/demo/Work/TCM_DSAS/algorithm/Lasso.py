#!/usr/bin/env python
# -*- coding:utf-8 -*-
#@Time    :    14:46  2019/12/9
#@Author  :    tb_youth
#@FileName:    Lasso.py
#@SoftWare:    PyCharm
#@Blog    :    http://blog.csdn.net/tb_youth



from sklearn import linear_model
import pandas as pd
import os
import numpy as np


'''
  Lasso的全称叫做Least absolute shrinkage and selection operator，
  直译过来为最小收缩与选择算子。
  其本质就是在常规的线性回归的基础上对参数加了一个L1正则化约束。
'''

def lasso(df,parameter_dict):
    x_labels = df.columns.values
    # y_lables = df.index.values

    x_data = df[x_labels[0:-1]]
    y_data = df[x_labels[-1]]

    lasso_model = linear_model.Lasso(alpha=parameter_dict.get('alpha'),max_iter=parameter_dict.get('max_iter'))
    lasso_model.fit(x_data,y_data)

    #权重系数，为0则代表该特征剔除
    # print(lasso_model.coef_)
    coef = pd.Series(lasso_model.coef_)

    #留下的特征数目
    print('选出的特征共{}个:'.format(sum(coef!=0)))

    #保存留下的特征
    best_features = []
    for i,item in enumerate(coef):
        if item != 0:
            feature = x_labels[i]
            best_features.append(feature)
            print(feature)
    #预测
    # print(lasso_model.predict(x_data.values[-1,np.newaxis]))
    return best_features
    
if __name__=='__main__':
    # print(os.getcwd())
    os.chdir('..')
    # print(os.getcwd())
    # print(os.path.abspath('.'))
    path = r'./data/data1.xlsx'
    df2 = pd.read_excel(path,index_col=0)
    parameter_dict = {
        'alpha':50,
        'max_iter':20000,
    }
    lasso(df2,parameter_dict)



