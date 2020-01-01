#!/usr/bin/env python
# -*- coding:utf-8 -*-
#@Time    :    17:26  2020/1/1
#@Author  :    tb_youth
#@FileName:    TuningAnalysis.py
#@SoftWare:    PyCharm
#@Blog    :    http://blog.csdn.net/tb_youth

'''
调参分析
'''

import os
import pandas as pd
from multiprocessing import Pool


from projects.demo.Work.TCM_DSAS.algorithm import FSFS


def getAimData(df, var_list, parameter_dict):
    f = FSFS.FSFSDemo(df, var_list, parameter_dict)
    f.run()
    RMSE, compare = f.analysis()
    feature_count = len(f.best_features)
    return list(RMSE) + [feature_count]


if __name__ == '__main__':

    os.chdir('..')
    file_name = 'data1.xlsx'
    path = '{0}\data\{1}'.format(os.path.abspath('.'), file_name)
    df = pd.read_excel(path, sheet_name='Sheet1', index_col=0)

    header_list = df.columns.values.tolist()
    var_list = [header_list[:-1], [header_list[-1]]]

    paramter_list = []
    for i in range(1, 8, 1):
        parameter_dict = {
            'topK': 100,
            'n_components': 3,
            'K': 10,
            'step': 10,
            'alp': i,
        }
        paramter_list.append(parameter_dict)

    res_list = []
    aim_list = []
    pool = Pool(6)
    for paramter in paramter_list:
        print(paramter)
        res = pool.apply_async(func=getAimData, args=(df, var_list, paramter,))
        res_list.append(res)

    for res in res_list:
        aim_list.append(res.get())

    pool.close()
    pool.join()

    print('*'*100)
    for data in aim_list:
        print(data)

    df = pd.DataFrame(data=aim_list,columns=["old_RMSE","now_RMSE","best_features_count"])
    #topK:100-5000,100
    #n_components:1-10,1
    #alp:1-7,1
    df.to_excel(excel_writer='./result/tuning_alp.xlsx',index=True,encoding='utf-8')
