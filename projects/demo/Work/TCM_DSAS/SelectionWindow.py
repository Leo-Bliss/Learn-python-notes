#!/usr/bin/env python
# -*- coding:utf-8 -*-
#@Time    :    15:43  2019/11/26
#@Author  :    tb_youth
#@FileName:    SelectionWindow.py
#@SoftWare:    PyCharm
#@Blog    :    http://blog.csdn.net/tb_youth

'''
特征选择窗口：
有设置参数功能
'''
import sys
from PyQt5.QtWidgets import QApplication,QWidget,QCompleter,QStatusBar
from PyQt5.QtWidgets import QLabel,QComboBox,QTextEdit,QLineEdit
from PyQt5.QtWidgets import QPushButton,QToolBar,QAction,QFileDialog
from PyQt5.QtWidgets import QHBoxLayout,QVBoxLayout
from PyQt5.QtGui import QIcon,QStandardItemModel
from PyQt5.QtCore import QThread,QObject,pyqtSignal,pyqtSlot,Qt

from projects.demo.Work.TCM_DSAS import AnalysisWindow
from projects.demo.Work.TCM_DSAS.algorithm import FSFS
from projects.demo.Work.TCM_DSAS.algorithm import Lasso
import SetParametersDemo
from projects.demo.Work.TCM_DSAS import DataFrameListMTF as DTL

class InitVarListThread(QThread):
    init_var_list_signal = pyqtSignal(list)
    end_signal = pyqtSignal()

    def __init__(self,model):
        super().__init__()
        self.model = model

    def run(self):
        rows = self.model.rowCount()
        columns = self.model.columnCount()
        self.var_list = []
        for row in range(rows):
            self.var_list = [self.model.index(row, column).data() for column in range(columns)
                             if self.model.index(row, column).data() not in ['',None]]
            self.init_var_list_signal.emit(self.var_list)
            break
        self.end_signal.emit()

class SelectionWindowdemo(QWidget):
    def __init__(self):
        super(SelectionWindowdemo,self).__init__()
        self.initUI()

    def initUI(self):
        self.resize(800,800)
        self.setWindowTitle('特征选择窗口')
        self.setWindowIcon(QIcon('./image/选择.png'))
        self.all_dict = None
        self.model = None
        self.y_predict = None
        self.df = None
        self.res_list = None
        self.var_list = []


        self.tool_bar = QToolBar()
        self.set_parameter = QAction(QIcon('./image/参数.png'),'设置参数',self)
        self.run = QAction(QIcon('./image/运行程序.png'),'运行程序',self)
        self.save = QAction(QIcon('./image/下载保存.png'),'保存结果',self)
        self.analysis = QAction(QIcon('./image/对比分析.png'),'分析预测',self)
        self.tool_bar.addAction(self.set_parameter)
        self.tool_bar.addAction(self.run)
        self.tool_bar.addAction(self.analysis)
        self.tool_bar.addAction(self.save)

        self.status_bar = QStatusBar()

        self.lable = QLabel('选择算法:')
        self.comb1 = QComboBox()
        algorithm_list = ['FSFS','Lasso']
        self.comb1.addItems(algorithm_list)
        # self.comb2 = QComboBox()
        # self.comb2.addItems(['算法','内容'])
        self.completer = QCompleter(algorithm_list)
        self.completer.setCompletionMode(QCompleter.UnfilteredPopupCompletion)
        self.line_edit = QLineEdit()
        self.line_edit.setCompleter(self.completer)
        self.button = QPushButton('搜索')

        hlayout = QHBoxLayout()
        hlayout.addWidget(self.lable)
        hlayout.addWidget(self.comb1)

        # hlayout.addWidget(self.comb2)
        hlayout.addWidget(self.line_edit)
        hlayout.addWidget(self.button)
        hlayout.addWidget(self.tool_bar)
        hlayout.addStretch(3)
        hlayout.setSpacing(10)
        self.text_edit = QTextEdit()
        file_name = "./other/aboutFSFS.txt"
        with open(file_name, 'r', encoding='utf-8') as f:
            text = f.read()
        self.text_edit.setText(text)
        self.text_edit.setReadOnly(True)
        self.run.setEnabled(False)

        vlayout = QVBoxLayout()
        vlayout.addItem(hlayout)
        vlayout.addWidget(self.text_edit)
        vlayout.addWidget(self.status_bar)
        self.setLayout(vlayout)

        self.comb1.currentIndexChanged.connect(self.selectionChange1)
        # self.comb2.currentIndexChanged(self.selecttionChange2)
        self.button.clicked.connect(self.clickSearch)
        self.set_parameter.triggered.connect(self.getParameter)
        self.run.triggered.connect(self.runProcess)
        self.analysis.triggered.connect(self.runAnalysis)
        self.save.triggered.connect(self.triggeredSave)

    #选择特征选择的算法时展示算法简介
    def selectionChange1(self):
        self.status_bar.showMessage(self.comb1.currentText(),5000)
        file_name = "./other/about{}.txt".format(self.comb1.currentText())
        text = ''
        try:
            with open(file_name,'r',encoding='utf-8') as f:
                text = f.read()
        except:
            pass
        self.text_edit.setText(text)

    #搜索算法
    def clickSearch(self):
        text = self.line_edit.text()
        index = self.comb1.findText(text)
        if index != -1:
            self.comb1.setCurrentIndex(index)
        else:
            print('没有找到{}'.format(text))

    def getModel(self,model):
        self.model = model

    def initVarList(self,var_list):
        self.var_list = var_list

    #获取参数对话框的相关参数
    def getParameter(self):
        if self.model == None:
            return
        self.init_var_list_thread = InitVarListThread(self.model)
        self.init_var_list_thread.init_var_list_signal.connect(self.initVarList)
        self.init_var_list_thread.end_signal.connect(self.initSetParametersDemo)
        self.init_var_list_thread.start()

    def initSetParametersDemo(self):
        self.init_var_list_thread.quit()
        index = self.comb1.currentIndex()
        self.dialog = SetParametersDemo.SetParameterDemo(index,self.var_list)
        self.dialog.sendSignal.sender.connect(self.setParameter)
        self.dialog.exec_()

    #设置算法的参数
    def setParameter(self,dic):
         self.all_dict = dic
         self.text_edit.setText('参数设置完成')
         self.run.setEnabled(True)

    def getRes(self,res_tuple):
        self.df,self.res_list, self.RMSE, self.y_predict = res_tuple
        str_res = ',\n'.join(self.res_list)
        res = '最终选择出的特征共{0}个:\n{1}'.format(len(self.res_list), str_res)
        self.text_edit.setText(res)



    def runFinished(self):
        #线程中的run未结束时，使用self.timer_thread.quit()是无效的
        self.timer_thread.is_running = False
        self.worker_thread.quit()
        print(self.timer_thread.isRunning())


    # 执行特征选择
    def runProcess(self):
        try:
            self.run.setEnabled(False)
            self.text_edit.setText('特征选择中...请您耐心等待...')
            algorithm = self.comb1.currentText()
            self.worker_thread = WorkerThread(self.model,self.all_dict,algorithm)
            self.timer_thread = TimerThread()
            self.worker_thread.res_signal.connect(self.getRes)
            self.worker_thread.finished_signal.connect(self.runFinished)
            self.worker_thread.start_signal.connect(self.timer_thread.start)
            self.timer_thread.start_signal.connect(self.showStatusBarMessage)
            self.worker_thread.start()
        except Exception as e:
            print(e)


    #执行数据分析
    def runAnalysis(self):
        self.plot_widget = AnalysisWindow.AnalysisWindowDemo()
        if self.y_predict is not None:
            self.plot_widget.RMSE = self.RMSE
            self.plot_widget.y_predict = self.y_predict
        self.plot_widget.setWindowModality(Qt.ApplicationModal)
        self.plot_widget.show()

    def showStatusBarMessage(self,msg):
        self.status_bar.showMessage(msg)

    #将选出的特征所对应的数据分离出来保存为单独的文件
    def triggeredSave(self):
        if self.res_list is None:
            return
        file_path, _ = QFileDialog.getSaveFileName(self, '保存文件',
                                                   './result','ALL Files(*);;xlsx(*.xlsx);;xls(*.xls);;csv(*.csv)')
        if file_path == '':
            return
        self.save_thread = SaveResThread(file_path,self.df,self.res_list)
        self.save_thread.start_save_signal.connect(self.showStatusBarMessage)
        self.save_thread.finished_signal.connect(self.save_thread.quit)
        self.save_thread.start()


class SaveResThread(QThread):
    start_save_signal = pyqtSignal(str)
    finished_signal = pyqtSignal()

    def __init__(self,file_path,df,res_list):
        super().__init__()
        self.file_path = file_path
        self.df = df
        self.res_list = res_list

    def run(self):
        self.start_save_signal.emit('开始保存..')
        try:
            best_features_df = self.df[self.res_list]
            # print(best_features_df)
            name, type = self.file_path.rsplit('.', maxsplit=1)
            best_features_df.to_excel(excel_writer='{}_best.{}'.format(name, type), index=True, encoding='utf-8')
            # print('-'*100)
            columns = self.df.columns.values.tolist()
            other_features_df = self.df[[column for column in columns if column not in self.res_list]]
            # print(other_features_df)
            other_features_df.to_excel(excel_writer='{}_other.{}'.format(name, type), index=True, encoding='utf-8')
            # print('保存完毕！')
            self.start_save_signal.emit('保存完毕！')
        except Exception as e:
            print(e)
        self.finished_signal.emit()

class TimerThread(QThread):
    start_signal = pyqtSignal(str)
    def __init__(self):
        super().__init__()
        self.sec = 0
        self.is_running = True
    def run(self):
        #这里最好不要使用while True
        while self.is_running:
            self.start_signal.emit('运行计时：{}秒'.format(self.sec))
            self.msleep(1000)
            self.sec += 1
        self.quit()

class WorkerThread(QThread):
    start_signal = pyqtSignal()
    finished_signal = pyqtSignal()
    res_signal = pyqtSignal(tuple)
    def __init__(self,model,all_dict,algorithm):
        super().__init__()
        self.model = model
        self.all_dict = all_dict
        self.algorithm = algorithm

    def run(self):
        self.start_signal.emit()
        dtl = DTL.DataFrameListMTF()
        self.data_list = dtl.model_to_list(self.model)
        self.df = dtl.list_to_DataFrame(self.data_list)
        try:
            f = None
            if self.algorithm == 'FSFS':
                f = FSFS.FSFSDemo(self.df, self.all_dict)
            elif self.algorithm == 'Lasso':
                f = Lasso.LassoDemo(self.df, self.all_dict)
            if f is None:
                return
            res_list = f.run()
            # 得到用于分析的数据
            RMSE, y_predict = f.analysis()
            res_tuple = (self.df,res_list, RMSE, y_predict)
            self.res_signal.emit(res_tuple)
        except Exception as e:
            print(e)

        #发送work完成信号
        self.finished_signal.emit()




if __name__=='__main__':
    app = QApplication(sys.argv)
    window = SelectionWindowdemo()
    window.show()
    sys.exit(app.exec_())