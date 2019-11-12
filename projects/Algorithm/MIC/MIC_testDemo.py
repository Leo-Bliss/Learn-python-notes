#!/usr/bin/env python
# -*- coding:utf-8 -*-
#@Time    :    10:14  2019/11/12
#@Author  :    tb_youth
#@FileName:    MIC_testDemo.py
#@SoftWare:    PyCharm
#@Blog    :    http://blog.csdn.net/tb_youth


'''
import numpy as np
from minepy import MINE

def print_stats(mine):
    print("MIC", mine.mic())


x = np.linspace(0, 1, 100)
print(x)
y = np.sin(10 * np.pi * x) + x
print(y)
mine = MINE(alpha=0.6, c=15)
mine.compute_score(x, y)

print("Without noise:")
print_stats(mine)


np.random.seed(0)
y += np.random.uniform(-1, 1, x.shape[0]) # add some noise
mine.compute_score(x, y)

print("With noise:")
print_stats(mine)
'''
import numpy as np
import pandas as pd
from minepy import MINE



# from sklearn.datasets import load_iris
# from sklearn.feature_selection import SelectKBest
#
# irisdata = load_iris()#加载scikit中的iris数据集

'''
iris数据集的中文名是安德森鸢尾花卉数据集，
英文全称是Anderson’s Iris data set。
iris包含150个样本，对应数据集的每行数据。
每行数据包含每个样本的四个特征和样本的类别信息，所以iris数据集是一个150行5列的二维表。
通俗地说，iris数据集是用来给花做分类的数据集，
每个样本包含了花萼长度、花萼宽度、花瓣长度、花瓣宽度四个特征（前4列），
我们需要建立一个分类器，
分类器可以通过样本的四个特征来判断样本属于山鸢尾、变色鸢尾还是维吉尼亚鸢尾（这三个名词都是花的品种）。
iris的每个样本都包含了品种信息，即目标属性（第5列，也叫target或label）。
'''
# def mic(x, y):
#     m = MINE()
#     m.compute_score(x, y)
#     return (m.mic(), 0.5)
#
#
# #选择 K 个最好的特征，返回特征选择后的数据
# irisdata_new =  SelectKBest(lambda X, Y: tuple(map(tuple,np.array(list(map(lambda x:mic(x, Y), X.T))).T)), k=3).fit_transform(irisdata.data, irisdata.target)
#
# print(irisdata.data.shape,irisdata_new.shape)
# print(irisdata_new)




def MIC_matirx(dataframe, mine):

    data = np.array(dataframe)
    n = len(data[0, :])
    result = np.zeros([n, n])

    for i in range(n):
        for j in range(n):
            mine.compute_score(data[:, i], data[:, j])
            result[i, j] = mine.mic()
            result[j, i] = mine.mic()
    RT = pd.DataFrame(result)
    return RT

# MIC结果矩阵可视化
import seaborn as sns
import matplotlib.pyplot as plt


def ShowHeatMap(DataFrame):
    colormap = plt.cm.RdBu  # 绘图库中的颜色查找表。比如A1是红色,A2是浅蓝色。 这样一种映射关系
    ylabels = DataFrame.columns.values.tolist()
    f, ax = plt.subplots(figsize=(14, 14))
    ax.set_title('GRA HeatMap')
    sns.heatmap(DataFrame.astype(float),
                cmap=colormap,
                ax=ax,
                annot=True,
                yticklabels=ylabels,
                xticklabels=ylabels)
    plt.show()



# 固定随机数，以确保每次生成的随机数固定
np.random.seed(42)

size = 750
#在0,1范围内随机生成size x 14的矩阵，自变量x
X = np.random.uniform(0, 1, (size, 14))

#"Friedamn #1” regression problem，单一因变量y
Y = (10 * np.sin(np.pi * X[:, 0] * X[:, 1]) + 20 * (X[:, 2] - .5)**2 +
     10 * X[:, 3] + 5 * X[:, 4] + np.random.normal(0, 1))

#Add 3 additional correlated variables (correlated with X1-X3)
X[:, 10:] = X[:, :4] + np.random.normal(0, .025, (size, 4))

names = ["x%s" % i for i in range(1, 15)]

# 构建生成DF数据集
Friedman_regression_data = pd.DataFrame(X)
Friedman_regression_data['y'] = Y
print(Friedman_regression_data)
# 获取MIC矩阵
mine = MINE(alpha=0.6, c=15)

# mine.compute_score(Friedman_regression_data[0],Friedman_regression_data['y'])
# print(mine.mic())

data_wine_mic = MIC_matirx(Friedman_regression_data, mine)
# 进行结果可视化
ShowHeatMap(data_wine_mic)
