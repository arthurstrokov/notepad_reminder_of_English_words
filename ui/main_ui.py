from PyQt5 import QtWidgets, uic

Form, Window = uic.loadUiType('ui/mydesign.ui')

if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    window = Window()
    form = Form()
    form.setupUi(window)
    window.show()
    app.exec_()
