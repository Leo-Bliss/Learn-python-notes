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
from minepy import MINE

class FSFS:
    def __init__(self,path):
        self.n_components = 3
        self.pls = PLSRegression(n_components=self.n_components,scale=True)
        self.path = path
        self.topK = 100
        self.step = 10
        self.alp = 5
        pass

    def run(self,k=10):
        df = pd.read_excel(self.path,sheet_name='Sheet1',index_col=0)

        #print(df.columns.values)
        #第一行，第一列
        header_list = list(df.columns.values)
        index_list = list(df.index.values)
        # print(header_list)
        # print(index_list)
        #自变量X，因变量y
        X = df[header_list[:-1]] #<class 'pandas.core.frame.DataFrame'>
        # print(X.shape)
        y = df[header_list[-1]] #<class 'pandas.core.series.Series'>
        # print(y.shape)

        #将数据分为k份，k折交叉验证
        kf = KFold(n_splits=k,shuffle=True,random_state=0)
        final_set_list = [] #经过k次折叠后得的特征集 列表
        for train_index,test_index in kf.split(X):
            # print(train_index)
            # print('+-------------------+')
            # print(test_index)
            X_train,y_train = X.values[train_index],y[train_index]
            y_train_tmp = np.array(y_train)

            #转换为DataFrame格式便于计算
            X_train = pd.DataFrame(X_train,index=train_index,columns=header_list[:-1])
            y_train = pd.DataFrame(y_train.values,index=train_index,columns=[header_list[-1]])

            X_test,y_test = X.values[test_index],y[test_index]
            # y_test_tmp = np.array(y_test)

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
            full_RMSE = get_RMSE(y_test_predict,y_test)
            print(full_RMSE)

            # Filter

            # #调python内置的方法
            # X_train_y = X_train.copy()
            # X_train_y[header_list[-1]] = y_train.values.copy()
            # # print(X_train_y.corr()[header_list[-1]])
            # dict_corr = (X_train_y.corr()[header_list[-1]]).to_dict()
            # # print(dict_corr)
            # lst_grade = sorted(dict_corr.items(),key=lambda x:abs(x[1]),reverse=True)
            # print(lst_grade[1:11])
            # print('....................................')

            full_sets = []
            #用自己写的方法
            #各特征与y1的相关系数，topK
            pearson_dict = {}
            for label in X_train:
                x_train_tmp = np.array(X_train[label])
                #计算每个特征与y的相关系数
                pearson_dict[label] = pearson(x_train_tmp,y_train_tmp)
            lst = sorted(pearson_dict.items(),key=lambda x:abs(x[1]),reverse=True)
            aim_lst = lst[:self.topK]
            full_sets.append(aim_lst)
            # print(aim_lst)
            print('+-----------------------------------------------------+')

            #特征的最大互信息系数
            mine = MINE(alpha=0.6,c=15)
            mic_dict = {}
            for label in X_train:
                x_train_tmp = np.array(X_train[label])
                # 计算每个特征与y的MIC
                mic_dict[label] = MIC(mine,x_train_tmp, y_train_tmp)
            mic_lst = sorted(mic_dict.items(), key=lambda x: x[1], reverse=True)
            aim_mic_lst = mic_lst[:self.topK]
            full_sets.append(aim_mic_lst)
            # print(aim_mic_lst)


            # Wrapper
            KFold_list = [] #第k次折叠得到的特征集
            for full_set in full_sets:
               best_RMSE = 1e18
               best_feature_num = 0
               for i in range(10,self.topK+1,10):
                   now_set = full_set[:i]
                   label_lst = [key for key, value in now_set]
                   # print(label_lst)
                   X_train_tmp = X_train[label_lst]
                   # print(X_train_tmp)
                   X_test_tmp = X_test[label_lst]
                   self.pls.fit(X_train_tmp, y_train)
                   y_test_predict_tmp = self.pls.predict(X_test_tmp)
                   RMSE_tmp = get_RMSE(y_test_predict_tmp, y_test)
                   if best_RMSE > RMSE_tmp:
                       best_RMSE, best_feature_num = RMSE_tmp, i
                   print(i,RMSE_tmp)
               if best_RMSE <  full_RMSE:
                   best_set_list = [label for label,r in full_set[:best_feature_num]]
                   KFold_list += best_set_list
                   # print(best_set_list)
               print('+++++++++++++++++++++++++++++++++++++++')
            # print(KFold_list)

            #Union
            final_set_list += list(set(KFold_list))

       #Voting
        condidate_features = set(final_set_list)
        print('候选特征有%d个'%len(condidate_features))
        condidate_feature_dict = {feature:final_set_list.count(feature) for feature in condidate_features}
        best_features = []
        for key,value in condidate_feature_dict.items():
            if(value >= self.alp):
                best_features.append(key)
            print(key+':'+str(value))
        print('最终投票出%d个特征'%len(best_features))
        print(best_features)

# RMSE：均方根误差，越小越好
def get_RMSE(y_predict, y_test):
    MSE = np.mean((y_test - y_predict) ** 2)
    RMSE = math.sqrt(MSE)
    return RMSE

# MIC:最大互信息系数
def MIC(mine, x, y):
    if (x.size != y.size):
        raise Exception('Both must be same size')
    mine.compute_score(x, y)
    return mine.mic()

# PLS
def PLS():
    pass

 #皮尔森相关系数
def pearson(vector1, vector2):
    if (vector1.shape != vector2.shape):
        raise Exception('Both vectors must be the same size')
    # 均值
    vector1_mean = vector1.mean()
    vector2_mean = vector2.mean()
    n = vector1.shape[0]
    if n == 0:
        raise Exception("The vector size is 0")
    # 协方差
    cov = sum((vector1 - vector1_mean) * (vector2 - vector2_mean)) / n
    # 方差乘积开方
    s = math.sqrt(np.var(vector1) * np.var(vector2))
    # 特判分母
    if s == 0:
        return 0.0
        # raise  Exception('div 0')
    r = cov / s
    return r


if __name__ == '__main__':
   path = r'\Learn-python-notes\material\科研实践\数据\data1.xlsx'
   f = FSFS(path)
   f.run()

