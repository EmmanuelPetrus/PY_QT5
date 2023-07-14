from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys

class MyWindow(QMainWindow):
    def __init__(self):
        super(MyWindow,self).__init__()
        self.initUI()
        self.setGeometry(600, 600, 500, 500)
        self.setWindowTitle("Robotics Operating System!!")

    def initUI(self):
        self.label = QtWidgets.QLabel(self)
        self.label.setText("My first label is active right now")
        self.label.move(70,70)
        self.label.adjustSize()

        self.b1 = QtWidgets.QPushButton(self)
        self.b1.setText("A new button!!")
        self.b1.clicked.connect(self.clicked)
    
    def clicked(self):
        self.label.setText("You clicked the button already fam")
        self.label.adjustSize()


def window():
    app = QApplication(sys.argv)
    win = MyWindow()
    

    win.show()
    sys.exit(app.exec_())

window()