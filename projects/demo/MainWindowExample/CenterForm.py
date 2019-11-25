#!/usr/bin/env python
# -*- coding:utf-8 -*-
#QDesktopWiget
import sys
from PyQt5.QtWidgets import QMainWindow,QApplication,QDesktopWidget
from PyQt5.QtGui import QIcon,QPixmap,QPalette,QBrush

from projects.demo.MainWindowExample import first_rc

class CenterForm(QMainWindow):
    def __init__(self,parent=None):
        super(CenterForm, self).__init__(parent)

        #set window title
        self.setWindowTitle('CenterWindow')

        #set window size
        self.resize(536,414)
        self.setMinimumSize(536,414)
        self.setMaximumSize(536,414)

        #set window statusBar
        self.status = self.statusBar()
        self.status.showMessage('status',5000)
        palette =  QPalette()
        pix = QPixmap(':/photos/space.png')
        palette.setBrush(QPalette.Background,QBrush(pix))
        self.setPalette(palette)
        #cnter
    def center(self):
        #screen coordinate
        screen = QDesktopWidget.screenGeometry()
        #window coordinate
        size = self.geometry()
        new_left = (screen.width()-size.width())/2
        new_top = (screen.height()-size.height())/2
        self.move(new_left,new_top)




if __name__ =='__main__':
    app = QApplication(sys.argv)
    window  = CenterForm()
    window.setWindowIcon(QIcon(':/photos/qq.png'))
    window.show()
    sys.exit(app.exec_())
