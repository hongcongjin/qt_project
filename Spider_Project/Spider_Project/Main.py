from PyQt5.QtWidgets import QApplication
from Connect_Ui_Signal import MainConnect
import sys
from PyQt5 import QtCore
import logging


if __name__ == '__main__':
    QtCore.QThread.currentThread().setObjectName('MainThread')
    logging.getLogger().setLevel(logging.DEBUG)
    app = QApplication(sys.argv)
    mainwindow = MainConnect()
    mainwindow.show()
    sys.exit(app.exec_())


