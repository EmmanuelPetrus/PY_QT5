# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'test5.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.popUp_button = QtWidgets.QPushButton(self.centralwidget)
        self.popUp_button.setGeometry(QtCore.QRect(320, 110, 221, 171))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.popUp_button.setFont(font)
        self.popUp_button.setObjectName("popUp_button")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.popUp_button.clicked.connect(self.show_popup)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.popUp_button.setText(_translate("MainWindow", "Pop-Up Button"))

    def show_popup(self):
        msg = QMessageBox()
        msg.setWindowTitle("Tutorial on PyQt5")
        msg.setText("This is the main test!")
        msg.setIcon(QMessageBox.Information)
        msg.setStandardButtons(QMessageBox.Cancel|QMessageBox.Ignore|QMessageBox.Retry)
        msg.setInformativeText("Informative text,yes oo!!!")

        msg.buttonClicked.connect(self.popbutton)

        msg.setDetailedText("details")
        msg.setDefaultButton(QMessageBox.Ignore)
        x = msg.exec_()
    
    def popbutton(self,i):
        print(i.text())


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
