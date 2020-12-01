# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Spider.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Ui_MainWindow(object):
    def setupUi(self, Ui_MainWindow):
        Ui_MainWindow.setObjectName("Ui_MainWindow")
        Ui_MainWindow.resize(720, 750)
        Ui_MainWindow.setMaximumSize(QtCore.QSize(720, 750))
        font = QtGui.QFont()
        font.setFamily("幼圆")
        font.setPointSize(12)
        Ui_MainWindow.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/新前缀/Icon.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Ui_MainWindow.setWindowIcon(icon)
        Ui_MainWindow.setWindowOpacity(0.92)
        Ui_MainWindow.setAutoFillBackground(True)
        Ui_MainWindow.setStyleSheet("background-image: url();\n"
"")
        Ui_MainWindow.setIconSize(QtCore.QSize(30, 30))
        Ui_MainWindow.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        self.centralwidget = QtWidgets.QWidget(Ui_MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(470, 50, 201, 51))
        self.comboBox.setStyleSheet("font: 12pt \"Arial Rounded MT Bold\";")
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setGeometry(QtCore.QRect(20, 10, 251, 141))
        self.scrollArea.setStyleSheet("")
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 232, 201))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.formLayout = QtWidgets.QFormLayout(self.scrollAreaWidgetContents)
        self.formLayout.setObjectName("formLayout")
        self.checkBox_2 = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setBold(True)
        font.setWeight(75)
        self.checkBox_2.setFont(font)
        self.checkBox_2.setObjectName("checkBox_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.checkBox_2)
        self.checkBox_3 = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setBold(True)
        font.setWeight(75)
        self.checkBox_3.setFont(font)
        self.checkBox_3.setObjectName("checkBox_3")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.checkBox_3)
        self.checkBox_4 = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setBold(True)
        font.setWeight(75)
        self.checkBox_4.setFont(font)
        self.checkBox_4.setObjectName("checkBox_4")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.checkBox_4)
        self.checkBox_5 = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        self.checkBox_5.setEnabled(False)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setBold(True)
        font.setWeight(75)
        self.checkBox_5.setFont(font)
        self.checkBox_5.setCheckable(True)
        self.checkBox_5.setObjectName("checkBox_5")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.checkBox_5)
        self.checkBox_6 = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        self.checkBox_6.setEnabled(False)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setBold(True)
        font.setWeight(75)
        self.checkBox_6.setFont(font)
        self.checkBox_6.setObjectName("checkBox_6")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.checkBox_6)
        self.checkBox_7 = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        self.checkBox_7.setEnabled(False)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setBold(True)
        font.setWeight(75)
        self.checkBox_7.setFont(font)
        self.checkBox_7.setObjectName("checkBox_7")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.checkBox_7)
        self.checkBox_1 = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setBold(True)
        font.setWeight(75)
        self.checkBox_1.setFont(font)
        self.checkBox_1.setObjectName("checkBox_1")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.checkBox_1)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.start = QtWidgets.QPushButton(self.centralwidget)
        self.start.setGeometry(QtCore.QRect(120, 360, 131, 51))
        self.start.setStyleSheet("font: 87 italic 16pt \"Bodoni MT Black\";\n"
"")
        self.start.setObjectName("start")
        self.queueNum = QtWidgets.QSpinBox(self.centralwidget)
        self.queueNum.setGeometry(QtCore.QRect(120, 290, 81, 41))
        self.queueNum.setMinimum(10)
        self.queueNum.setMaximum(48)
        self.queueNum.setObjectName("queueNum")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(30, 300, 51, 20))
        font = QtGui.QFont()
        font.setFamily("Century Schoolbook")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setGeometry(QtCore.QRect(20, 430, 681, 31))
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.progressBar.setFont(font)
        self.progressBar.setProperty("value", 0)
        self.progressBar.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.progressBar.setTextVisible(True)
        self.progressBar.setOrientation(QtCore.Qt.Horizontal)
        self.progressBar.setInvertedAppearance(False)
        self.progressBar.setObjectName("progressBar")
        self.keyword = QtWidgets.QLineEdit(self.centralwidget)
        self.keyword.setGeometry(QtCore.QRect(120, 180, 531, 31))
        font = QtGui.QFont()
        font.setFamily("幼圆")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.keyword.setFont(font)
        self.keyword.setWhatsThis("")
        self.keyword.setText("")
        self.keyword.setReadOnly(False)
        self.keyword.setClearButtonEnabled(True)
        self.keyword.setObjectName("keyword")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(30, 170, 91, 51))
        font = QtGui.QFont()
        font.setFamily("Century Schoolbook")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.savepath = QtWidgets.QLineEdit(self.centralwidget)
        self.savepath.setGeometry(QtCore.QRect(120, 230, 531, 31))
        font = QtGui.QFont()
        font.setFamily("幼圆")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.savepath.setFont(font)
        self.savepath.setText("")
        self.savepath.setDragEnabled(False)
        self.savepath.setClearButtonEnabled(True)
        self.savepath.setObjectName("savepath")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(30, 220, 91, 51))
        font = QtGui.QFont()
        font.setFamily("Century Schoolbook")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.imageNum = QtWidgets.QSpinBox(self.centralwidget)
        self.imageNum.setGeometry(QtCore.QRect(410, 290, 81, 41))
        self.imageNum.setMinimum(0)
        self.imageNum.setMaximum(9999999)
        self.imageNum.setObjectName("imageNum")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(250, 300, 121, 20))
        font = QtGui.QFont()
        font.setFamily("Century Schoolbook")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit.setGeometry(QtCore.QRect(20, 480, 681, 231))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(10)
        self.plainTextEdit.setFont(font)
        self.plainTextEdit.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(134, 207, 255, 196), stop:1 rgba(255, 255, 255, 255));")
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.cancel = QtWidgets.QPushButton(self.centralwidget)
        self.cancel.setGeometry(QtCore.QRect(510, 360, 131, 51))
        self.cancel.setAutoFillBackground(True)
        self.cancel.setStyleSheet("font: 87 italic 16pt \"Bodoni MT Black\";")
        self.cancel.setObjectName("cancel")
        Ui_MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(Ui_MainWindow)
        self.checkBox_2.clicked['bool'].connect(self.checkBox_1.setDisabled)
        self.checkBox_4.clicked['bool'].connect(self.checkBox_3.setDisabled)
        QtCore.QMetaObject.connectSlotsByName(Ui_MainWindow)

    def retranslateUi(self, Ui_MainWindow):
        _translate = QtCore.QCoreApplication.translate
        Ui_MainWindow.setWindowTitle(_translate("Ui_MainWindow", "MainWindow"))
        self.comboBox.setItemText(0, _translate("Ui_MainWindow", "Insert&Download"))
        self.comboBox.setItemText(1, _translate("Ui_MainWindow", "Insert to DB"))
        self.comboBox.setItemText(2, _translate("Ui_MainWindow", "Download from DB"))
        self.checkBox_2.setText(_translate("Ui_MainWindow", "Google Similar"))
        self.checkBox_3.setText(_translate("Ui_MainWindow", "Bing"))
        self.checkBox_4.setText(_translate("Ui_MainWindow", "Bing Similar"))
        self.checkBox_5.setText(_translate("Ui_MainWindow", "Flickr"))
        self.checkBox_6.setText(_translate("Ui_MainWindow", "Instagram"))
        self.checkBox_7.setText(_translate("Ui_MainWindow", "GettyImage"))
        self.checkBox_1.setText(_translate("Ui_MainWindow", "Google"))
        self.start.setText(_translate("Ui_MainWindow", "Start"))
        self.label_7.setText(_translate("Ui_MainWindow", "Queue"))
        self.keyword.setToolTip(_translate("Ui_MainWindow", "<html><head/><body><p align=\"center\">Different Keys Split With &quot;|&quot;</p></body></html>"))
        self.keyword.setPlaceholderText(_translate("Ui_MainWindow", "Input keywords, seperated by  \' | \' "))
        self.label_4.setText(_translate("Ui_MainWindow", "Keyword"))
        self.savepath.setPlaceholderText(_translate("Ui_MainWindow", "Input savepath for Images"))
        self.label_5.setText(_translate("Ui_MainWindow", "SavePath"))
        self.label_6.setText(_translate("Ui_MainWindow", "MaxNum / Key"))
        self.cancel.setText(_translate("Ui_MainWindow", "Cancel"))
import icon_rc
import spider_rc