#!/usr/bin/env python
# -*- coding:utf-8 -*-
#@Time    :    10:29  2020/1/2
#@Author  :    tb_youth
#@FileName:    VisualAnalysis.py
#@SoftWare:    PyCharm
#@Blog    :    http://blog.csdn.net/tb_youth

'''
将调参结果绘制可视化图形
'''

import matplotlib.pyplot as plt
import pandas as pd

def draw1_RMSE(df):
    columns = df.columns.values.tolist()

    # 中文乱码处理
    plt.rcParams['font.sans-serif'] = ['SimHei']
    plt.rcParams['axes.unicode_minus'] = False
    x = [str(i) for i in range(100, 1001, 100)]
    data = df[columns[1]].values[:len(x)]
    plt.plot(x, data, marker='*', mec='r', label='now_RMSE')
    plt.plot(x,df[columns[0]].values[:len(x)],label='old_RMSE')
    plt.legend()
    plt.xlabel('TopK')
    plt.ylabel('RMSE')
    plt.xticks(x)
    plt.title('RMSE随TopK变化趋势')

    # 标上数值，数值保留小数点后两位
    for x, y in enumerate(data):
        plt.text(x, y+4, '{:.2f}'.format(y), ha='center')

    # plt.savefig("./result/data1_topK_RMSE.svg",dpi=600,format='svg')
    plt.show()

def draw2_RMSE(df):
    columns = df.columns.values.tolist()

    # 中文乱码处理
    plt.rcParams['font.sans-serif'] = ['SimHei']
    plt.rcParams['axes.unicode_minus'] = False
    x = [str(i) for i in range(50, 401, 50)]
    data = df[columns[1]].values[:len(x)]
    plt.plot(x, data, marker='*', mec='r', label='now_RMSE')
    plt.plot(x,df[columns[0]].values[:len(x)],label='old_RMSE')
    plt.legend()
    plt.xlabel('TopK')
    plt.ylabel('RMSE')
    plt.xticks(x)
    plt.title('RMSE随TopK变化趋势')

    # 标上数值，数值保留小数点后两位
    for x, y in enumerate(data):
        plt.text(x, y+4, '{:.2f}'.format(y), ha='center')

    # plt.savefig("./result/data2_topK_RMSE.svg",dpi=600,format='svg')
    plt.show()

def draw1_featureCnt(df):
    columns = df.columns.values.tolist()


    # 中文乱码处理
    plt.rcParams['font.sans-serif'] = ['SimHei']
    plt.rcParams['axes.unicode_minus'] = False
    x = [str(i) for i in range(100, 1001, 100)]
    data = df[columns[2]].values[:len(x)]
    plt.plot(x, data, marker='^', mec='r', label='best_features_count')
    plt.legend()
    plt.xlabel('TopK')
    plt.ylabel('feature_count')
    plt.xticks(x)
    plt.title('best_features数量随TopK变化趋势')

    # 标上数值，数值保留小数点后两位
    for x, y in enumerate(data):
        plt.text(x, y-8, '{}'.format(y), ha='center')

    #plt.savefig("./result/data1_topK_features_cnt.svg", dpi=600, format='svg')
    plt.show()

def draw1_n_components_features_cnt(df):
    columns = df.columns.values.tolist()

    # 中文乱码处理
    plt.rcParams['font.sans-serif'] = ['SimHei']
    plt.rcParams['axes.unicode_minus'] = False
    x = [str(i) for i in range(1, 11, 1)]
    data = df[columns[2]].values[:len(x)]
    plt.plot(x, data, marker='^', mec='r', label='best_features_count')
    plt.legend()
    plt.xlabel('n_components')
    plt.ylabel('feature_count')
    plt.xticks(x)
    plt.title('best_features数量随n_components变化趋势')

    # 标上数值，数值保留小数点后两位
    for x, y in enumerate(data):
        plt.text(x, y+1, '{}'.format(y), ha='center')

    # plt.savefig("./result/data1_n_components_features_cnt.svg", dpi=600, format='svg')
    plt.show()

def draw1_n_components_RMSE(df):
    columns = df.columns.values.tolist()

    # 中文乱码处理
    plt.rcParams['font.sans-serif'] = ['SimHei']
    plt.rcParams['axes.unicode_minus'] = False
    x = [str(i) for i in range(1, 11, 1)]
    data = df[columns[1]].values[:len(x)]
    plt.plot(x, data, marker='*', mec='r', label='now_RMSE')
    data2 = df[columns[0]].values[:len(x)]
    plt.plot(x, data2,marker='+',mec='b', label='old_RMSE')
    plt.legend()
    plt.xlabel('n_components')
    plt.ylabel('RMSE')
    plt.xticks(x)
    plt.title('RMSE随n_components变化趋势')

    # 标上数值，数值保留小数点后两位
    for x, y in enumerate(data):
        plt.text(x, y+1, '{:.2f}'.format(y), ha='center')
    for x,y in enumerate(data2):
        plt.text(x,y+4,'{:.2f}'.format(y), ha='center')
    # plt.savefig("./result/data1_n_components_RMSE.svg", dpi=600, format='svg')
    plt.show()

def draw1_alp_features_cnt(df):
    columns = df.columns.values.tolist()

    # 中文乱码处理
    plt.rcParams['font.sans-serif'] = ['SimHei']
    plt.rcParams['axes.unicode_minus'] = False
    x = [str(i) for i in range(1, 8, 1)]
    data = df[columns[2]].values[:len(x)]
    plt.plot(x, data, marker='^', mec='r', label='best_features_count')
    plt.legend()
    plt.xlabel('alp')
    plt.ylabel('feature_count')
    plt.xticks(x)
    plt.title('best_features数量随alp变化趋势')

    # 标上数值，数值保留小数点后两位
    for x, y in enumerate(data):
        plt.text(x, y+2, '{}'.format(y), ha='center')

    # plt.savefig("./result/data1_alp_features_cnt.svg", dpi=600, format='svg')
    plt.show()

def draw1_alp_RMSE(df):
    columns = df.columns.values.tolist()

    # 中文乱码处理
    plt.rcParams['font.sans-serif'] = ['SimHei']
    plt.rcParams['axes.unicode_minus'] = False
    x = [str(i) for i in range(1, 8, 1)]
    data = df[columns[1]].values[:len(x)]
    plt.plot(x, data, marker='*', mec='r', label='now_RMSE')
    data2 = df[columns[0]].values[:len(x)]
    plt.plot(x, data2,label='old_RMSE')
    plt.legend()
    plt.xlabel('alp')
    plt.ylabel('RMSE')
    plt.xticks(x)
    plt.title('RMSE随alp变化趋势')

    # 标上数值，数值保留小数点后两位
    for x, y in enumerate(data):
        plt.text(x, y+4, '{:.2f}'.format(y), ha='center')

    plt.savefig("./result/data1_alp_RMSE.svg", dpi=600, format='svg')
    plt.show()

def draw2_featureCnt(df):
    columns = df.columns.values.tolist()
    indexs = df.index.tolist()

    # 中文乱码处理
    plt.rcParams['font.sans-serif'] = ['SimHei']
    plt.rcParams['axes.unicode_minus'] = False
    x = [str(i) for i in range(50, 401, 50)]
    data = df[columns[2]].values[:len(x)]
    plt.plot(x, data, marker='^', mec='r', label='best_features_count')
    plt.legend()
    plt.xlabel('TopK')
    plt.ylabel('feature_count')
    plt.xticks(x)
    plt.title('best_features数量随TopK变化趋势')

    # 标上数值，数值保留小数点后两位
    for x, y in enumerate(data):
        plt.text(x, y-9, '{}'.format(y), ha='center')

    #plt.savefig("./result/data2_topK_features_cnt.svg", dpi=600, format='svg')
    plt.show()

def draw2_n_components_features_cnt(df):
    columns = df.columns.values.tolist()

    # 中文乱码处理
    plt.rcParams['font.sans-serif'] = ['SimHei']
    plt.rcParams['axes.unicode_minus'] = False
    x = [str(i) for i in range(1, 11, 1)]
    data = df[columns[2]].values[:len(x)]
    plt.ylim(40,75)
    plt.plot(x, data, marker='^', mec='r', label='best_features_count')
    plt.legend()
    plt.xlabel('n_components')
    plt.ylabel('feature_count')
    plt.xticks(x)
    plt.title('best_features数量随n_components变化趋势')

    # 标上数值，数值保留小数点后两位
    for x, y in enumerate(data):
        plt.text(x, y+1, '{}'.format(y), ha='center')

    plt.savefig("./result/data2_n_components_features_cnt.svg", dpi=600, format='svg')
    plt.show()

def draw2_n_components_RMSE(df):
    columns = df.columns.values.tolist()

    # 中文乱码处理
    plt.rcParams['font.sans-serif'] = ['SimHei']
    plt.rcParams['axes.unicode_minus'] = False
    x = [str(i) for i in range(1, 11, 1)]
    data = df[columns[1]].values[:len(x)]
    plt.plot(x, data, marker='*', mec='r', label='now_RMSE')
    data2 = df[columns[0]].values[:len(x)]
    plt.ylim(500,1900)
    plt.plot(x, data2,marker='+',mec='b', label='old_RMSE')
    plt.legend()
    plt.xlabel('n_components')
    plt.ylabel('RMSE')
    plt.xticks(x)
    plt.title('RMSE随n_components变化趋势')

    # 标上数值，数值保留小数点后两位
    for x, y in enumerate(data):
        plt.text(x, y-50, '{:.2f}'.format(y), ha='center')
    for x,y in enumerate(data2):
        plt.text(x,y+50,'{:.2f}'.format(y), ha='center')
    # plt.savefig("./result/data2_n_components_RMSE.svg", dpi=600, format='svg')
    plt.show()

def draw2_alp_features_cnt(df):
    columns = df.columns.values.tolist()

    # 中文乱码处理
    plt.rcParams['font.sans-serif'] = ['SimHei']
    plt.rcParams['axes.unicode_minus'] = False
    x = [str(i) for i in range(1, 8, 1)]
    data = df[columns[2]].values[:len(x)]
    plt.plot(x, data, marker='^', mec='r', label='best_features_count')
    plt.legend()
    plt.xlabel('alp')
    plt.ylabel('feature_count')
    plt.xticks(x)
    plt.title('best_features数量随alp变化趋势')

    # 标上数值，数值保留小数点后两位
    for x, y in enumerate(data):
        plt.text(x, y+2, '{}'.format(y), ha='center')

    # plt.savefig("./result/data2_alp_features_cnt.svg", dpi=600, format='svg')
    plt.show()

def draw2_alp_RMSE(df):
    columns = df.columns.values.tolist()

    # 中文乱码处理
    plt.rcParams['font.sans-serif'] = ['SimHei']
    plt.rcParams['axes.unicode_minus'] = False
    x = [str(i) for i in range(1, 8, 1)]
    data = df[columns[1]].values[:len(x)]
    plt.ylim(600,950)
    plt.plot(x, data, marker='*', mec='r', label='now_RMSE')
    data2 = df[columns[0]].values[:len(x)]
    plt.plot(x, data2,label='old_RMSE')
    plt.legend()
    plt.xlabel('alp')
    plt.ylabel('RMSE')
    plt.xticks(x)
    plt.title('RMSE随alp变化趋势')

    # 标上数值，数值保留小数点后两位
    for x, y in enumerate(data):
        plt.text(x, y+4, '{:.2f}'.format(y), ha='center')

    # plt.savefig("./result/data2_alp_RMSE.svg", dpi=600, format='svg')
    plt.show()


if __name__=='__main__':
    # file = './result/tuning_topK.xlsx'
    # file = './result/tuning_topK2.xlsx'
    # file = './result/tuning_n_components.xlsx'
    # file = './result/tuning_n_components2.xlsx'
    # file = './result/tuning_alp.xlsx'
    file = './result/tuning_alp2.xlsx'
    df = pd.read_excel(file,sheet_name='Sheet1', index_col=0)

    # draw1_RMSE(df)
    # draw1_featureCnt(df)
    # draw1_n_components_features_cnt(df)
    # draw1_n_components_RMSE(df)
    # draw1_alp_features_cnt(df)
    # draw1_alp_RMSE(df)

    # draw2_RMSE(df)
    # draw2_featureCnt(df)
    # draw2_n_components_features_cnt(df)
    # draw2_n_components_RMSE(df)
    # draw2_alp_features_cnt(df)
    draw2_alp_RMSE(df)


