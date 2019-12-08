#-*-coding=utf-8-*-

#自动补全
import sys
from PyQt5.QtWidgets import QApplication, QCompleter, QLineEdit
from PyQt5.QtCore import QStringListModel


def get_data(model):
    model.setStringList(["completion", "data", "goes", "here", "cu1609", "cu1610", "cu1611"])

if __name__ == "__main__":
    app = QApplication(sys.argv)
    edit = QLineEdit()
    completer = QCompleter()
    edit.setCompleter(completer)

    model = QStringListModel()
    completer.setModel(model)
    get_data(model)

    edit.show()
    sys.exit(app.exec_())