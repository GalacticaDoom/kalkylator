# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'calculator.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from ast import main
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def add1(self):
        self.textEdit.setText(self.textEdit.toPlainText()+"1")
    def add2(self):
        self.textEdit.setText(self.textEdit.toPlainText()+"2")
    def add3(self):
        self.textEdit.setText(self.textEdit.toPlainText()+"3")
    def add4(self):
        self.textEdit.setText(self.textEdit.toPlainText()+"4")
    def add5(self):
        self.textEdit.setText(self.textEdit.toPlainText()+"5")
    def add6(self):
        self.textEdit.setText(self.textEdit.toPlainText()+"6")
    def add7(self):
        self.textEdit.setText(self.textEdit.toPlainText()+"7")
    def add8(self):
        self.textEdit.setText(self.textEdit.toPlainText()+"8")
    def add9(self):
        self.textEdit.setText(self.textEdit.toPlainText()+"9")
    def add0(self):
        self.textEdit.setText(self.textEdit.toPlainText()+"0")
    def addplus(self):
        self.textEdit.setText(self.textEdit.toPlainText()+"+")
    def addminus(self):
        self.textEdit.setText(self.textEdit.toPlainText()+"-")
    def adddelenie(self):
        self.textEdit.setText(self.textEdit.toPlainText()+"/")
    def addprocent(self):
        self.textEdit.setText(self.textEdit.toPlainText()+"%")
    def addkoren(self):
        try:
            self.textEdit.setText(str(eval(self.textEdit.toPlainText())**0.5))
        except:
            self.textEdit.setText("")
            self.textEdit.setPlaceholderText('ERROR')
    def addstepen(self):
        self.textEdit.setText(self.textEdit.toPlainText()+"^")
    def addpoint(self):
        self.textEdit.setText(self.textEdit.toPlainText()+".")
    def addumnoj(self):
        self.textEdit.setText(self.textEdit.toPlainText()+"*")
    def addskobka1(self):
        self.textEdit.setText(self.textEdit.toPlainText()+"(")
    def addskobka2(self):
        self.textEdit.setText(self.textEdit.toPlainText()+")")
    def ravno(self):
        try:
            self.textEdit.setText(str(eval(self.textEdit.toPlainText())))
        except:
            self.textEdit.setText("")
            self.textEdit.setPlaceholderText('ERROR')
    def clear(self):
        self.textEdit.setText("")
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(817, 638)
        MainWindow.setStyleSheet("background-color: rgb(100, 100, 100);color:rgb(255, 255, 255)")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(290, 0, 191, 51))
        font = QtGui.QFont()
        font.setPointSize(17)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(90, 160, 131, 61))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.add1)
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(240, 160, 131, 61))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.add2)
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(390, 160, 131, 61))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.clicked.connect(self.add3)
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(90, 230, 131, 61))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_4.clicked.connect(self.add4)
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(390, 230, 131, 61))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_5.clicked.connect(self.add6)
        self.pushButton_7 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_7.setGeometry(QtCore.QRect(390, 300, 131, 61))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_7.setFont(font)
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_7.clicked.connect(self.add9)
        self.pushButton_8 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_8.setGeometry(QtCore.QRect(240, 230, 131, 61))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_8.setFont(font)
        self.pushButton_8.setObjectName("pushButton_8")
        self.pushButton_8.clicked.connect(self.add5)
        self.pushButton_9 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_9.setGeometry(QtCore.QRect(240, 300, 131, 61))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_9.setFont(font)
        self.pushButton_9.setObjectName("pushButton_9")
        self.pushButton_9.clicked.connect(self.add8)
        self.pushButton_10 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_10.setGeometry(QtCore.QRect(90, 300, 131, 61))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_10.setFont(font)
        self.pushButton_10.setObjectName("pushButton_10")
        self.pushButton_10.clicked.connect(self.add7)
        self.pushButton_11 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_11.setGeometry(QtCore.QRect(390, 370, 131, 61))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_11.setFont(font)
        self.pushButton_11.setObjectName("pushButton_11")
        self.pushButton_11.clicked.connect(self.clear)
        self.pushButton_12 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_12.setGeometry(QtCore.QRect(240, 370, 131, 61))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_12.setFont(font)
        self.pushButton_12.setObjectName("pushButton_12")
        self.pushButton_12.clicked.connect(self.add0)
        self.pushButton_13 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_13.setGeometry(QtCore.QRect(90, 370, 131, 61))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_13.setFont(font)
        self.pushButton_13.setObjectName("pushButton_13")
        self.pushButton_13.clicked.connect(self.ravno)
        self.pushButton_14 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_14.setGeometry(QtCore.QRect(540, 370, 131, 61))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_14.setFont(font)
        self.pushButton_14.setObjectName("pushButton_14")
        self.pushButton_14.clicked.connect(self.addplus)
        self.pushButton_15 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_15.setGeometry(QtCore.QRect(540, 160, 131, 61))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_15.setFont(font)
        self.pushButton_15.setObjectName("pushButton_15")
        self.pushButton_15.clicked.connect(self.adddelenie)
        self.pushButton_16 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_16.setGeometry(QtCore.QRect(540, 300, 131, 61))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_16.setFont(font)
        self.pushButton_16.setObjectName("pushButton_16")
        self.pushButton_16.clicked.connect(self.addminus)
        self.pushButton_17 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_17.setGeometry(QtCore.QRect(540, 230, 131, 61))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_17.setFont(font)
        self.pushButton_17.setObjectName("pushButton_17")
        self.pushButton_17.clicked.connect(self.addumnoj)
        self.pushButton_18 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_18.setGeometry(QtCore.QRect(540, 440, 131, 61))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_18.setFont(font)
        self.pushButton_18.setObjectName("pushButton_18")
        self.pushButton_18.clicked.connect(self.addkoren)
        self.pushButton_19 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_19.setGeometry(QtCore.QRect(390, 440, 131, 61))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_19.setFont(font)
        self.pushButton_19.setObjectName("pushButton_19")
        self.pushButton_19.clicked.connect(self.addstepen)
        self.pushButton_20 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_20.setGeometry(QtCore.QRect(90, 440, 131, 61))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_20.setFont(font)
        self.pushButton_20.setObjectName("pushButton_20")
        self.pushButton_20.clicked.connect(self.addpoint)
        self.pushButton_21 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_21.setGeometry(QtCore.QRect(240, 440, 131, 61))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_21.setFont(font)
        self.pushButton_21.setObjectName("pushButton_21")
        self.pushButton_21.clicked.connect(self.addprocent)
        self.pushButton_22 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_22.setGeometry(QtCore.QRect(240, 510, 131, 61))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_22.setFont(font)
        self.pushButton_22.setObjectName("pushButton_22")
        self.pushButton_22.clicked.connect(self.addskobka2)
        self.pushButton_23 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_23.setGeometry(QtCore.QRect(90, 510, 131, 61))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_23.setFont(font)
        self.pushButton_23.setObjectName("pushButton_23")
        self.pushButton_23.clicked.connect(self.addskobka1)
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(110, 70, 521, 61))
        self.textEdit.setObjectName("textEdit")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 817, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Калькулятор"))
        self.pushButton.setText(_translate("MainWindow", "1"))
        self.pushButton.setStyleSheet('''QPushButton:hover{background-color:blue;}QPushButton{background-color:gray}''')
        self.pushButton_2.setText(_translate("MainWindow", "2"))
        self.pushButton_2.setStyleSheet('''QPushButton:hover{background-color:blue;}QPushButton{background-color:gray}''')
        self.pushButton_3.setText(_translate("MainWindow", "3"))
        self.pushButton_3.setStyleSheet('''QPushButton:hover{background-color:blue;}QPushButton{background-color:gray}''')
        self.pushButton_4.setText(_translate("MainWindow", "4"))
        self.pushButton_4.setStyleSheet('''QPushButton:hover{background-color:blue;}QPushButton{background-color:gray}''')
        self.pushButton_5.setText(_translate("MainWindow", "6"))
        self.pushButton_5.setStyleSheet('''QPushButton:hover{background-color:blue;}QPushButton{background-color:gray}''')
        self.pushButton_7.setText(_translate("MainWindow", "9"))
        self.pushButton_7.setStyleSheet('''QPushButton:hover{background-color:blue;}QPushButton{background-color:gray}''')
        self.pushButton_8.setText(_translate("MainWindow", "5"))
        self.pushButton_8.setStyleSheet('''QPushButton:hover{background-color:blue;}QPushButton{background-color:gray}''')
        self.pushButton_9.setText(_translate("MainWindow", "8"))
        self.pushButton_9.setStyleSheet('''QPushButton:hover{background-color:blue;}QPushButton{background-color:gray}''')
        self.pushButton_10.setText(_translate("MainWindow", "7"))
        self.pushButton_10.setStyleSheet('''QPushButton:hover{background-color:blue;}QPushButton{background-color:gray}''')
        self.pushButton_11.setText(_translate("MainWindow", "C"))
        self.pushButton_11.setStyleSheet('''QPushButton:hover{background-color:blue;}QPushButton{background-color:gray}''')
        self.pushButton_12.setText(_translate("MainWindow", "0"))
        self.pushButton_12.setStyleSheet('''QPushButton:hover{background-color:blue;}QPushButton{background-color:gray}''')
        self.pushButton_13.setText(_translate("MainWindow", "="))
        self.pushButton_13.setStyleSheet('''QPushButton:hover{background-color:blue;}QPushButton{background-color:gray}''')
        self.pushButton_14.setText(_translate("MainWindow", "+"))
        self.pushButton_14.setStyleSheet('''QPushButton:hover{background-color:blue;}QPushButton{background-color:gray}''')
        self.pushButton_15.setText(_translate("MainWindow", "/"))
        self.pushButton_15.setStyleSheet('''QPushButton:hover{background-color:blue;}QPushButton{background-color:gray}''')
        self.pushButton_16.setText(_translate("MainWindow", "-"))
        self.pushButton_16.setStyleSheet('''QPushButton:hover{background-color:blue;}QPushButton{background-color:gray}''')
        self.pushButton_17.setText(_translate("MainWindow", "x"))
        self.pushButton_17.setStyleSheet('''QPushButton:hover{background-color:blue;}QPushButton{background-color:gray}''')
        self.pushButton_18.setText(_translate("MainWindow", "√"))
        self.pushButton_18.setStyleSheet('''QPushButton:hover{background-color:blue;}QPushButton{background-color:gray}''')
        self.pushButton_19.setText(_translate("MainWindow", "^"))
        self.pushButton_19.setStyleSheet('''QPushButton:hover{background-color:blue;}QPushButton{background-color:gray}''')
        self.pushButton_20.setText(_translate("MainWindow", "."))
        self.pushButton_20.setStyleSheet('''QPushButton:hover{background-color:blue;}QPushButton{background-color:gray}''')
        self.pushButton_21.setText(_translate("MainWindow", "%"))
        self.pushButton_21.setStyleSheet('''QPushButton:hover{background-color:blue;}QPushButton{background-color:gray}''')
        self.pushButton_22.setText(_translate("MainWindow", ")"))
        self.pushButton_22.setStyleSheet('''QPushButton:hover{background-color:blue;}QPushButton{background-color:gray}''')
        self.pushButton_23.setText(_translate("MainWindow", "("))
        self.pushButton_23.setStyleSheet('''QPushButton:hover{background-color:blue;}QPushButton{background-color:gray}''')


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())