import sys
from PyQt5.QtWidgets import QHBoxLayout,QMainWindow,QApplication,QPushButton,QWidget

class QuitApplication(QMainWindow):
    def __init__(self):
        super(QuitApplication,self).__init__()
        self.resize(300,120)
        self.setWindowTitle('退出应用程序')

        # 添加Button

        self.button1 = QPushButton('退出应用程序')
        # 将信号与槽关联
        self.button1.clicked.connect(self.onClick_Button)

        #创建水平布局
        layout = QHBoxLayout()
        #将控件加入水平布局
        layout.addWidget(self.button1)

        #创建主框架
        mainFrame = QWidget()
        #将布局加入主框架中
        mainFrame.setLayout(layout)
        #把主框架放到整个窗口上
        self.setCentralWidget(mainFrame)

    # 按钮单击事件的方法（自定义的槽）
    def onClick_Button(self):
        sender = self.sender()
        print(sender.text() + ' 按钮被按下')
        app = QApplication.instance()
        # 退出应用程序
        app.quit()
if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = QuitApplication()
    main.show()
    sys.exit(app.exec_())