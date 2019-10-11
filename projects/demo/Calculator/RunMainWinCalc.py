#!/usr/bin/env python
# -*- coding:utf-8 -*-
import sys
from projects.demo.Calculator import calc
from PyQt5.QtWidgets import QApplication,QMainWindow
if __name__ =='__main__':
    app = QApplication(sys.argv)
    mainWindow = QMainWindow()
    ui = calc.Ui_widget()
    ui.setupUi(mainWindow)
    mainWindow.show()
    sys.exit(app.exec_())
