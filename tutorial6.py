from PyQt5.QtWidgets import QApplication,QWidget
import sys

class MainWindow(QWidget):
    def init(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setWindowTitle("Simple example 1")
        self.resize(230, 254)
        self.show()


def winshow():
    qApp = QApplication(sys.argv)

    w = MainWindow()

    sys.exit(app.exec_())

winshow()