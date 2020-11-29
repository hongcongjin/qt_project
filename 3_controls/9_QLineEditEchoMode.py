'''

QLineEdit控件与回显模式

基本功能：输入单行的文本

EchoMode（回显模式）

4种回显模式(像输入密码会自动隐藏)

1. Normal
2. NoEcho
3. Password
4. PasswordEchoOnEdit


Mac : Command    Windows:Control
'''
from PyQt5.QtWidgets import *
import sys

class QLineEditEchoMode(QWidget) :
    def __init__(self):
        super(QLineEditEchoMode,self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('文本输入框的回显模式')
        #使用表单布局
        formLayout = QFormLayout()

        normalLineEdit = QLineEdit()
        noEchoLineEdit = QLineEdit()
        passwordLineEdit = QLineEdit()
        passwordEchoOnEditLineEdit = QLineEdit()

        formLayout.addRow("Normal",normalLineEdit)
        formLayout.addRow("NoEcho", noEchoLineEdit)
        formLayout.addRow("Password",passwordLineEdit)
        formLayout.addRow("PasswordEchoOnEdit",passwordEchoOnEditLineEdit)

        # placeholdertext
        #设置默认提示，什么都没有输入默认灰色字体提示
        normalLineEdit.setPlaceholderText("Normal")
        noEchoLineEdit.setPlaceholderText("NoEcho")
        passwordLineEdit.setPlaceholderText("Password")
        passwordEchoOnEditLineEdit.setPlaceholderText("PasswordEchoOnEdit")

        normalLineEdit.setEchoMode(QLineEdit.Normal)
        noEchoLineEdit.setEchoMode(QLineEdit.NoEcho)
        passwordLineEdit.setEchoMode(QLineEdit.Password)
        passwordEchoOnEditLineEdit.setEchoMode(QLineEdit.PasswordEchoOnEdit)

        self.setLayout(formLayout)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = QLineEditEchoMode()
    main.show()
    sys.exit(app.exec_())
