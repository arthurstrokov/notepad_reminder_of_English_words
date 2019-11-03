import PyQt5
from PyQt5 import QtWidgets
from mydesign import Ui_MainWindow
from service import show_random_word_from_file_json
import sys


class MyWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        # connecting the clicked signal with btnClicked slot
        self.ui.pushButton.clicked.connect(self.btnClicked)

    def btnClicked(self):
        file_name = 'data/two_thousand_most_frequently_used_words_of_the_english_language.json'
        word = show_random_word_from_file_json(file_name)
        self.ui.label.setText(word)


if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    application = MyWindow()
    application.show()
    sys.exit(app.exec())
