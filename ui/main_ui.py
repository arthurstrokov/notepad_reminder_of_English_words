from PyQt5 import uic
from PyQt5 import QtCore, QtGui, QtWidgets


Form, Window = uic.loadUiType('mydesign.ui')

if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    window = Window()
    form = Form()
    form.setupUi(window)
    window.show()
    app.exec_()
