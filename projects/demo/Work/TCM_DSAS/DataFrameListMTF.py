#!/usr/bin/env python
# -*- coding:utf-8 -*-
#@Time    :    15:17  2019/12/13
#@Author  :    tb_youth
#@FileName:    DataFrameListMTF.py
#@SoftWare:    PyCharm
#@Blog    :    http://blog.csdn.net/tb_youth

'''
DataFrame 和 list 相互转换,
包括DataFrame的index与columns，
DataFrameListMutualTransform: DataFrameListMTF
加入QStandardModel转换为list，
list_to_DataFrame作出变更，
要求导入数据格式不满足dataFrame格式（需要去掉样本标识）。
'''
import pandas as pd

class DataFrameListMTF():
    def __init__(self):
        pass

    def list_to_DataFrame(self,lst):
        df = pd.DataFrame(lst)
        column_list = list(df.iloc[0, 0:])
        data = df.iloc[1:, 0:]
        data.columns = column_list
        return data.reset_index()

    def DataFrame_to_list(self,df):
        data_list = [[''] + df.columns.values.tolist()]
        index_list = df.index.values.tolist()
        for i, item in enumerate(df.values.tolist()):
            data_list.append([index_list[i]] + item)
        return data_list

    def judege_num(self,num):
        try:
            float(num)
            return True
        except:
            return False

    def model_to_list(self, model):
        rows = model.rowCount()
        columns = model.columnCount()
        data_list = []
        for row in range(rows):
            row_values = []
            for column in range(columns):
                cell = model.index(row, column).data()
                if cell is None:
                    break
                if self.judege_num(cell) is True:
                    cell = float(cell)
                row_values.append(cell)
            if len(row_values) == 0:
                continue
            data_list.append(row_values)
        return data_list
