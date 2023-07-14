from PyQt5 import QtWidgets
# app = QtWidgets.QWidget(windowTitle = "Hello Qt")
# print(app.windowTitle());

app = QtWidgets.QApplication([])
window = QtWidgets.QWidget()
window.setWindowTitle("Hello Qt")
print(window.windowTitle())

window.show()
app.exec()