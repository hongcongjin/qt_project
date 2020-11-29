import sys
# import qt_test
import GridLayout
import MainWinAbsoluteLayout
import Buddy
import TabOrder
import closewindows
import MenuToobar
from PyQt5.QtWidgets import QApplication,QMainWindow

if __name__ == '__main__':
    app=QApplication(sys.argv)
    mainWindow=QMainWindow()
    ui=MenuToobar.Ui_MainWindow()
    #向主窗口上添加控件
    ui.setupUi(mainWindow)
    mainWindow.show()
    sys.exit(app.exec_())










